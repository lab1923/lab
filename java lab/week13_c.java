import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;

public class Week13_c {
  public static void main(String... s) throws Exception {
    Csv csv = new Csv();
  }
}

class Csv extends JFrame implements ActionListener {
  JComboBox<String> deptBox;
  JFileChooser fileChooser;
  JTextArea t;
  JButton b1, b2;
  String[][] fileInfo = new String[100][100];
  HashSet<String> deptSet = new HashSet<String>();
  int id = 0;

  Csv() {

    b1 = new JButton("Open File");
    b1.addActionListener(this);
    b1.setBounds(40, 10, 100, 20);
    add(b1);

    b2 = new JButton("Generate");
    b2.setBounds(280, 10, 100, 20);
    add(b2);
    b2.setVisible(false);

    t = new JTextArea(10, 50);
    t.setBounds(10, 40, 450, 200);
    add(t);

    deptBox = new JComboBox();
    deptBox.addItem("None");
    deptBox.setBounds(160, 10, 100, 20);
    deptBox.setVisible(false);

    b2.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        if (deptBox.getSelectedItem() == "None") {
          t.setText("Select something");
        } else {
          String value = deptBox.getSelectedItem().toString();
          String data = "name | rollno | dept " + "\n";
          for (int i = 0; i < 100; i++) {
            if (value == fileInfo[i][2]) {
              data = data + fileInfo[i][0] + " | " + fileInfo[i][1] + " | " + fileInfo[i][2] + "\n";
            }
          }
          t.setText(data);
        }
      }
    });

    add(deptBox);
    setLayout(null);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setSize(500, 350);
    setVisible(true);
    setLocationRelativeTo(null);
  }

  public void actionPerformed(ActionEvent ae) {
    fileChooser = new JFileChooser(System.getProperty("user.dir"));
    int response = fileChooser.showOpenDialog(this);
    String line = "";
    if (response == JFileChooser.APPROVE_OPTION) {
      deptBox.setVisible(true);
      b2.setVisible(true);
      try {
        File file = fileChooser.getSelectedFile();
        BufferedReader br = new BufferedReader(new FileReader(file));
        while ((line = br.readLine()) != null) {
          String dept[] = line.split(",");
          if (!deptSet.contains(dept[2]))
            deptBox.addItem(dept[2]);
          deptSet.add(dept[2]);
          fileInfo[id][0] = dept[0];
          fileInfo[id][1] = dept[1];
          fileInfo[id][2] = dept[2];
          id++;
        }
      } catch (Exception e) {
      }
    }
  }
}