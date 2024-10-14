/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplicationnew;

import jade.core.AID;
import jade.core.Agent;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;
import jade.wrapper.AgentController;
import jade.wrapper.ContainerController;
import jade.wrapper.StaleProxyException;
import static java.lang.Math.random;
import java.util.Random;

/**
 *
 * @author Marzieh
 */
public class JavaApplicationNew {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        // Start the JADE platform
        Runtime runtime = Runtime.instance();
        Profile profile = new ProfileImpl();

        profile.setParameter(Profile.MAIN_HOST, "localhost"); // Set the host (replace with your IP address if needed)
        profile.setParameter(Profile.MAIN_PORT, "1099"); // Set the port number explicitly
        profile.setParameter(Profile.GUI, "true"); // Enable the GUI
        profile.setParameter(Profile.PLATFORM_ID, "new-platform");

        ContainerController containerController = runtime.createMainContainer(profile);

        // Create and add Traffic Light Agents to the container
        try {
            for (int i = 0; i < 10; i++) {

//                AgentController agentController = containerController.createNewAgent(
//                        String.valueOf(i), TrafficLightAgent.class.getName(), null);
//                agentController.start();
                //System.out.println(agentController.getName()+"**********");
                Object[] arg = new Object[]{i};
                AgentController agentController = containerController.createNewAgent(
                        String.valueOf(i), TrafficLightAgent.class.getName(), arg);
                agentController.start();

            }
        } catch (StaleProxyException e) {
            e.printStackTrace();
        }

//        //Environment:
//        // Create an instance of Random class
//        Random random = new Random();
//        // Create an array to store the locations of the cars
//        int[] carLocations = new int[30];
//        // 30 cars
//        for (int i = 0; i < 30; i++) {
//            // Generate a random location between 0 and 9 for each car
//            int locationOfCar = random.nextInt(10);
//            // Store the location of the car in the array
//            carLocations[i] = locationOfCar;
//        }
    }

    public static class TrafficLightAgent extends Agent {

        private int greenTime;
        private int redTime;
        private int yellowTime;
        private String id;
        private int carsStopped;
        private int nextNeighbor;
        private int prevNeighbor;
        private double utility;
        public int trafficlight_no;

        public TrafficLightAgent() {
            this.setup();
        }

        private void calculateUtility() {
            // Adjust the calculation based on your requirements
            utility = 1.0 / (carsStopped + 1); // Example formula
        }

        private void sendSensorMessage(int passingCars) {
            ACLMessage msg = new ACLMessage(ACLMessage.INFORM);
            AID nextNeighborAID = new AID("" + nextNeighbor, AID.ISLOCALNAME);
            msg.addReceiver(nextNeighborAID);
            msg.setContent("Sense:" + passingCars);
            send(msg);
        }

        private void sendUpdateMessageToPrev() {
            ACLMessage msg = new ACLMessage(ACLMessage.REQUEST);
            AID prevNeighborAID = new AID("" + prevNeighbor, AID.ISLOCALNAME);
            msg.addReceiver(prevNeighborAID);
            msg.setContent("Update:" + 0);
            send(msg);
        }

        private void sendUpdateMessageToNext() {
            ACLMessage msg = new ACLMessage(ACLMessage.REQUEST);
            AID nextNeighborAID = new AID("" + nextNeighbor, AID.ISLOCALNAME);
            msg.addReceiver(nextNeighborAID);
            msg.setContent("Update:" + 1);
            send(msg);
        }

        protected void setup() {
            // Initialize the agent's variables
            greenTime = 20; // in seconds
            redTime = 30; // in seconds
            yellowTime = 5; // in seconds
            //System.out.println(this.getLocalName()+"**********");

            //environment (cars):
            //There are (randomly) 0 to 10 cars stopped before each of the trafficLights
            Random random = new Random();
            carsStopped = random.nextInt(11);
            //System.out.println(this.getLocalName()+" -> number of cars before it: "+carsStopped+"**********"+id);

            id = this.getLocalName();
            //System.out.println(this.getLocalName() + "**********");
            //System.out.println(id + "**********");

            Object[] arg = getArguments();
            if (arg != null && arg.length > 0) {
                trafficlight_no = (int) arg[0];
            }
            //System.out.println(id + "**********"+trafficlight_no);

            //set neighbors
            nextNeighbor = (trafficlight_no + 1) % 10;
            if (trafficlight_no > 0) {
                prevNeighbor = trafficlight_no - 1;
            } else {
                prevNeighbor = 9;
            }

            // Add a ticker behavior to periodically change the traffic light color
            addBehaviour(new TickerBehaviour(this, 1000) {
                private int timeLeft = greenTime;
                private String color = "green";

                protected void onTick() {
                    // Decrement the time left for the current color
                    timeLeft--;
                    //System.out.println("timeLeft=" + timeLeft);

                    if (timeLeft == 0) {
                        //System.out.println(getLocalName()+" -> number of cars before it: "+carsStopped+"**********");
                        // Switch to the next color
                        calculateUtility();
                        if (utility < 0.25) { // more than 3 cars are stopped
                            sendUpdateMessageToPrev();
                            sendUpdateMessageToNext();
                            greenTime++;
                        }

                        switch (color) {
                            case "green":
                                color = "yellow";
                                sendSensorMessage(Math.min((greenTime / 4), carsStopped));
                                carsStopped = Math.max(0, carsStopped - (greenTime / 4));
                                //System.out.println("yellow");
                                //System.out.println(getLocalName() + " is yellow");
                                timeLeft = yellowTime;
                                break;
                            case "yellow":
                                color = "red";
                                //System.out.println("red");
                                //System.out.println(getLocalName() + " is red");
                                timeLeft = redTime;
                                break;
                            case "red":
                                color = "green";
                                //System.out.println("green");
                                //System.out.println(getLocalName() + " is green");
                                timeLeft = greenTime;
                                break;
                        }
                    }
                }
            });

            addBehaviour(new CyclicBehaviour(this) {
                public void action() {
                    ACLMessage msg = receive();
                    if (msg != null) {
                        // Process the message
                        String content = msg.getContent();
                        //System.out.println(content);
                        if (content.startsWith("Sense:")) {
                            // Extract the ID from the message
                            int passingCars = Integer.parseInt(content.substring(6));
                            carsStopped = carsStopped + passingCars;
                        } else if (content.startsWith("Update:")) {
                            // Extract the ID from the message
                            int prevOrNext = Integer.parseInt(content.substring(7));
                            Random random = new Random();
                            int uncertainty = random.nextInt(2);
                            if (prevOrNext == 0) { //you are the previous
                                if (utility > 0.25 && greenTime >= 15 && redTime <= 30 && uncertainty == 1) { //autonomy
                                    greenTime--;
                                    redTime++;
                                }
                            } else if (prevOrNext == 1) { // you are the next
                                if (utility > 0.25 && redTime >= 15 && greenTime <= 30) { //autonomy
                                    greenTime++;
                                    redTime--;
                                }
                            }
                        }
                    } else {
                        block();
                    }
                }
            });
        }
    }
}
