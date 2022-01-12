import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.awt.event.*;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextArea;
import javax.swing.JTextField;
 
class RunMe extends JFrame{

    private static JFrame f;
    private static int w, h;
    static JTextField inputText;
    private static JButton searchButton;
    static JTextArea resultsDisplay;
    
    static void getResults(String query) throws IOException {
        Thread myThread = new Thread(new pythonRunner(), "python thread");
        myThread.start();
        // myThread.run();
        // String results = "";
        // long startTime = System.currentTimeMillis();
        // long nextTime = startTime;
        // resultsDisplay.setText("Searching");
        // Process process = Runtime.getRuntime().exec("python3 test.py " + query);
        // BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        // BufferedReader errors = new BufferedReader(new InputStreamReader(process.getErrorStream()));
        // resultsDisplay.setText("Actually Searching now");
        // while (process.isAlive()) {
        //     if (System.currentTimeMillis() > nextTime) {
        //         nextTime = System.currentTimeMillis() + ((long) Math.random() * (long) 2500) + (long) 2500;
        //         System.out.print("Interogating the citizens for reviews on attractions\n");
        //         resultsDisplay.setText(resultsDisplay.getText() + "Interogating the citizens for reviews on attractions\n");
        //     }
        // }
        // System.out.println("about to wait");
        // // process.waitFor();
        // System.out.println("frick it im done waiting");
        // String line;
        // while ((line = reader.readLine()) != null) {
        //     results += line + "\n";
        // }
        // while ((line = errors.readLine()) != null) {
        //     System.out.println(line);
        // }
        // // resultsDisplay.setText(results);
        // System.out.println(results);
        // return results;
    }
 
    public static void main(String args[]) throws IOException {
        w = 1000;
        h = 1000;
        f = new JFrame("Attraction finder");
        f.setSize(w, h);
        f.setTitle("Vector Grahpics");
        f.setLayout(null);
        inputText = new JTextField("search for real life attractions anywhere in Florida\n ex: Top tourist attractions in Orlando, Hotels in Tampa, Things to do in Miami, Italian Restaurants in Tampa");
        searchButton = new JButton("Search");
        resultsDisplay = new JTextArea("no results to display yet");
        searchButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                try {
                    getResults(inputText.getText());
                } catch (IOException e1) {
                    System.out.println("uhhhh you messed up buddy, try connecting to the internet?");
                }
                System.out.println("search completed");
            }
        });
        inputText.setBounds(100, 200, 300, 50);
        searchButton.setBounds(300, 350, 100, 50);
        resultsDisplay.setBounds(500, 200, 400, 600);
        resultsDisplay.setAutoscrolls(true);
        resultsDisplay.setWrapStyleWord(true);
        resultsDisplay.setLineWrap(true);
        f.add(resultsDisplay);
        f.add(inputText);
        f.add(searchButton);            
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
}
}

class pythonRunner implements Runnable {

    @Override
    public void run() {
        // String[] waitingMessages = new String[]{
        //     "Searching the internet far and wide",
        //     "interrogating citizens for reviews",
        //     "Diving to the depths of the oceans for possible underwater hotels",
        //     "looking into hotels in oribit",
        //     "Do you think the International Space station is a good hotel?",
        //     "Sorry, still searching",
        //     "Currently wondering if something is wrong with the program or this wifi is just slow",
        //     "Stealing information from tripadvisor",
        //     "double checking information",
        //     "assuring only the best of the best attractions are displayed" };
        String results = "";
        long nextTime = System.currentTimeMillis();
        int frameLength = 500;
        int i = 0;
        String query = RunMe.inputText.getText();
        Process process;
        try {
            process = Runtime.getRuntime().exec("python3 test.py " + query);
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            BufferedReader errors = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            // RunMe.resultsDisplay.setText("Starting the search of a lifetime\n");
            String message;
            while (process.isAlive()) {
                if (System.currentTimeMillis() - nextTime > frameLength) {
                    message = "Searching";
                    for (int x = 0; x < i; x++) {
                        message += ". ";
                    }
                    nextTime = System.currentTimeMillis();
                    i = (i+1)%6;
                    // System.out.print(message + "\n");
                    RunMe.resultsDisplay.setText(message);
                }
            }
            // System.out.println("about to wait");
            // process.waitFor();
            // System.out.println("im done waiting");
            String line;
            i = 0;
            while ((line = reader.readLine()) != null) {
                i++;
                results += "#" + i + ")  " + line + "\n";
            }
            while ((line = errors.readLine()) != null) {
                System.out.println(line);
            }
            RunMe.resultsDisplay.setText(results);
            if (results == "") {
                RunMe.resultsDisplay.setText("Nothing found, please try again with another query");
            }
            System.out.println(results);
        } 
        catch (IOException e) {
        }
    }
    
}