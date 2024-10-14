/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package multiagent_pbl3;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;
import jade.core.AID;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.behaviours.CyclicBehaviour;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;
import java.util.ArrayList;
import java.util.List;

import java.util.Random;

/**
 *
 * @author Marzieh
 */
public class MultiAgent_PBL3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        // Start the JADE platform
        jade.core.Runtime runtime = jade.core.Runtime.instance();
        Profile profile = new ProfileImpl();
        AgentContainer container = runtime.createMainContainer(profile);

        // Create and add Traffic Light Agents to the container
        try {
            for (int i = 0; i < 10; i++) {
                AgentController agentController = container.createNewAgent("TrafficLightAgent" + i, TrafficLightAgent.class.getName(), new Object[]{i});
                agentController.start();
            }
        } catch (StaleProxyException e) {
            e.printStackTrace();
        }

    }

    public static class TrafficLightAgent extends Agent {

        private int greenTime;
        private int redTime;
        private int yellowTime;
//        private String[] neighbors;
        private Random rand;
        private int carsStopped;
        private int carsPassing;
        private double utility;
        private int id;
//        private Car[] cars;
        private AID leftNeighbor;
        private AID rightNeighbor;
        private List<Car> cars; // Replace Car[] cars with List<Car> cars


        public TrafficLightAgent(int id) {
            this.id = id;
            this.setup();
        }

        protected void setup() {
            // Initialize the agent's variables
            greenTime = 20; // in seconds
            redTime = 30; // in seconds
            yellowTime = 5; // in seconds
            //neighbors = new String[]{"TrafficLightAgent1", "TrafficLightAgent2"}; // names of neighboring traffic lights
            rand = new Random();
            carsStopped = 0;
            carsPassing = 0;
            cars = new ArrayList<>(); // Initialize the cars list

//            // Get the ID of the agent
//            Object[] args = getArguments();
//            if (args != null && args.length > 0) {
//                id = (int) args[0];
//            }

//            cars = new Car[10];
            // Set neighbors
            if (id > 0) {
                leftNeighbor = new AID("TrafficLightAgent" + (id - 1), AID.ISLOCALNAME);
            }
            if (id < 9) {
                rightNeighbor = new AID("TrafficLightAgent" + (id + 1), AID.ISLOCALNAME);
            }

            // Add a ticker behavior to periodically change the traffic light color
            addBehaviour(new TickerBehaviour(this, 1000) {
                private int timeLeft = greenTime;
                private String color = "green";

                protected void onTick() {
                    // Decrement the time left for the current color
                    timeLeft--;
                    if (timeLeft == 0) {
                        // Switch to the next color
                        switch (color) {
                            case "green":
                                color = "yellow";
                                timeLeft = yellowTime;
                                break;
                            case "yellow":
                                color = "red";
                                timeLeft = redTime;
                                break;
                            case "red":
                                color = "green";
                                timeLeft = greenTime;
                                break;
                        }
                    }

                    // Check if the number of cars parked behind this traffic light exceeds a certain number
                    if (carsStopped > 5) {

                        if (leftNeighbor != null) {
                            requestUpdate(leftNeighbor);
                        }
                        if (rightNeighbor != null) {
                            requestUpdate(rightNeighbor);
                        }

//                        if (redTime > 5) {
//                            redTime--;
//                        }
//                        if (greenTime < 30) {
//                            greenTime++;
//                        }
//
//                        // Send a message to the previous agent (neighbor)
//                        if (id != 0) {
//                            ACLMessage msg = new ACLMessage(ACLMessage.INFORM);
//                            int recID = id - 1;
//                            AID receiver = new AID("TrafficLightAgent" + recID, AID.ISLOCALNAME);
//                            msg.addReceiver(receiver);
//                            msg.setContent("update:" + recID);
//                            send(msg);
//                        }
                    }

                    // Update the state of traffic flow based on cars stopped or passing by
//                    Car cars[] = null;
                    updateTrafficFlow(); //***(cars);
                }

            });

            // Add a behaviour to receive messages
            addBehaviour(new CyclicBehaviour(this) {
                public void action() {
                    ACLMessage msg = receive();
                    if (msg != null) {
                        // Process the message
                        String content = msg.getContent();
                        if (content.startsWith("update:")) {

                            // Extract the ID from the message
                            int senderID = Integer.parseInt(content.substring(7));
                            if (senderID == id - 1 || senderID == id + 1) {
                                adjustTimings();
                            }

//                            // Extract the ID from the message
//                            int recID = Integer.parseInt(content.substring(7));
//                            if (greenTime > 5) {
//                                greenTime--;
//                            }
//                            if (redTime < 30) {
//                                redTime++;
//                            }
                        }
                    } else {
                        block();
                    }
                }
            });

        }

        private void requestUpdate(AID neighbor) {
            ACLMessage msg = new ACLMessage(ACLMessage.REQUEST);
            msg.addReceiver(neighbor);
            msg.setContent("update:" + id);
            send(msg);
        }

        private void adjustTimings() {
            if (redTime > 5) {
                redTime--;
            }
            if (greenTime < 30) {
                greenTime++;
            }
        }

        public void updateTrafficFlow() {
            int stoppedCount = 0;
            int passingCount = 0;

            for (Car car : cars) {
                if (car != null) {
                    if (car.isStopped()) {
                        stoppedCount++;
                    } else {
                        passingCount++;
                    }
                }
            }
            // Update the state variables
            carsStopped = stoppedCount;
            carsPassing = passingCount;
            // Assuming utility calculation is based on stopped cars count
            utility = 1.0 / (carsStopped + 1);

        }

        public int isGreen() {
            if (greenTime != 0) {
                return 1;
            } else {
                return 0;
           }

        }
    } 

    public class Car {

        private int speed;
        private int positionX;
        private int positionY;
        private String direction;
        private boolean isStopped;

        public Car(int speed, int positionX, int positionY, String direction) {
            this.speed = speed;
            this.positionX = positionX;
            this.positionY = positionY;
            this.direction = direction;
            this.isStopped = false;
        }

        public Car() {
        }

        public void move(TrafficLightAgent trafficLightAgent) {
            int flag = trafficLightAgent.isGreen();
            if (trafficLightAgent.isGreen() == 0) {
                isStopped = true;
                return;
            }
            // logic for car movement
            // update position based on speed and direction
        }

    }

}
