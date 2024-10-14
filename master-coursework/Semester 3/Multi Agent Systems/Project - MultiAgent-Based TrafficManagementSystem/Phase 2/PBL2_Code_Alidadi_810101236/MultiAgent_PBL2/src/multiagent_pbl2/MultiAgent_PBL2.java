/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package multiagent_pbl2;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;
import java.util.Random;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;
import java.util.ArrayList;

/**
 *
 * @author Marzieh
 */
public class MultiAgent_PBL2 {

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
                AgentController agentController
                        = container.createNewAgent("TrafficLightAgent"
                                + i, TrafficLightAgent.class.getName(), null);
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
        private String[] neighbors;
        private Random rand;
        private int carsStopped;
        private int carsPassing;
        private int utility;
        private Car[] cars;


        protected void setup() {
            // Initialize the agent's variables
            greenTime = 20; // in seconds
            redTime = 30; // in seconds
            yellowTime = 5; // in seconds
            neighbors = new String[]{"intersection1", "intersection2"}; // names of neighboring traffic lights
            rand = new Random();
            carsStopped = 0;
            carsPassing = 0;
            cars = new Car[10]; // Initialize cars array with a fixed size


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

                    // Update the state of traffic flow based on cars stopped or passing by
//                    Car[] cars = new Car[numCars];
//                    ArrayList<Car> cars = new ArrayList<>();
                    updateTrafficFlow(cars);
                }

//                private void updateTrafficFlow() {
//                    // Logic to update the state of traffic flow based on cars stopped or passing by
//                    // For example, increment carsStopped if a car stops at the traffic light
//                    // It can also communicate with neighboring traffic lights to coordinate traffic flow
//
//                    // Assume carsStopped and carsPassing are variables tracking the number of cars stopped and passing by
//                    int carsStopped = 0; // Get the number of cars stopped at the traffic light
//                    int carsPassing = 0; // Get the number of cars passing by the traffic light
//
//                    // Update the state of traffic flow based on cars stopped or passing by
//                    if (carsStopped > 0) {
//                        // Update traffic flow state for stopped cars
//                        // For example, set a flag to indicate that cars are stopped at the traffic light
//                    }
//
//                    if (carsPassing > 0) {
//                        // Update traffic flow state for passing cars
//                        // For example, adjust traffic signal timing or coordination with neighboring lights
//                    }
//                }
            });
        }

        public void updateTrafficFlow(Car[] cars) {
            for (Car car : cars) {
                if (car.isStopped()) {
                    carsStopped++;
//                    utility = 1 / (carsStopped + 1);
                } else {
                    carsPassing++;
                }
            }
            // logic for updating traffic flow state based on stopped and passing counts
        }

        private double calculateUtility(int carsStopped) {
            // Adjust the calculation based on your requirements
            return 1.0 / (carsStopped + 1); // Example formula
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
        private boolean stopped;

//        public Car(int speed, int positionX, int positionY, String direction) {
//            this.speed = speed;
//            this.positionX = positionX;
//            this.positionY = positionY;
//            this.direction = direction;
//            this.isStopped = false;
//        }

        
        public Car() {
            this.speed = 0;
            this.positionX = 0;
            this.positionY = 0;
            this.direction = "";
            this.stopped = false;
        }
        
        public boolean isStopped() {
            return stopped;
        }

        public void setStopped(boolean stopped) {
            this.stopped = stopped;
        }

//        public void move(TrafficLightAgent trafficLightAgent) {
//            int flag = trafficLightAgent.isGreen();
//            if (trafficLightAgent.isGreen() == 0) {
//                isStopped = true;
//                return;
//            }
//            // logic for car movement
//            // update position based on speed and direction
//        }

    }

}
