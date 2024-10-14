/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package multiagent_pbl1_v2;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import java.util.Random;
import jade.core.AID;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.behaviours.Behaviour;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.wrapper.StaleProxyException;

/**
 *
 * @author Marzieh
 */
public class MultiAgent_PBL1_V2 {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        
        // Start the JADE platform
        jade.core.Runtime runtime = jade.core.Runtime.instance();
        Profile profile = new ProfileImpl();
        
        profile.setParameter(Profile.MAIN_HOST, "localhost"); // Set the host (replace with your IP address if needed)
        profile.setParameter(Profile.GUI, "true"); // Enable the GUI
        
        AgentContainer container = runtime.createMainContainer(profile);
        
        // Create and add Traffic Light Agents to the container
        try {
            for (int i = 0; i < 10; i++) {
                AgentController agentController = container.createNewAgent("TrafficLightAgent" + i, TrafficLightAgent.class.getName(), null);
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
//        private Random rand;
        
        private void TrafficLightAgent(){
        
//            this.declareStatus();
        }
        
        

        protected void setup() {
            // Initialize the agent's variables
            greenTime = 20; // in seconds
            redTime = 30; // in seconds
            yellowTime = 5; // in seconds
//            neighbors = new String[]{"intersection1", "intersection2"}; // names of neighboring traffic lights
//            rand = new Random();

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
                }
            });

        }
        
        protected void declareStatus(){
            
            System.out.println(this.getName());
            
        }
        

    }  
     
    //Design the Environment
    public class Street {
        // Define street properties, such as name, length, etc.
    
        // Implement methods to handle traffic light states and interactions with cars
    }

    public class Car {
        // Define car properties and behaviors
    }
    
}
