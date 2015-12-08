import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class day7 {

    Hashtable<String, Integer> numbers = new Hashtable<String, Integer>();
    String fileName = "input.txt";

    public int find(String search){

        if(search.matches("^-?\\d+$")){
            return (Integer.parseInt(search) & 0xffff);
        }
        try {
            File file = new File(this.fileName);
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line;
            while ((line = bufferedReader.readLine()) != null) {

                String [] y = line.split(" ");
                String oWire = y[y.length - 1];
                int result = 0;
                if(oWire.equals(search)){
                    if(numbers.get(search) != null){
                        return numbers.get(search);
                    }
                    if (line.contains("RSHIFT")) {
                        fileReader.close();
                        result = (find(y[0]) >> Integer.parseInt(y[2]));
                    } else if (line.contains("LSHIFT")) {
                        fileReader.close();
                        result = (find(y[0]) << Integer.parseInt(y[2]));
                    } else if (line.contains("OR")) {
                        fileReader.close();
                        result = find(y[0]) | find(y[2]);
                    } else if (line.contains("AND")) {
                        fileReader.close();
                        result = find(y[0]) & find(y[2]);
                    } else if (line.contains("NOT")) {
                        fileReader.close();
                        result = ~find(y[1]);
                    } else {
                        fileReader.close();
                        result = find(y[0]);
                    }
                    result = result & 0xffff;

                    numbers.put(search,result);
                    return result;
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return Short.parseShort("1");
    }
    public static void main(String[] args) {

        day7 myday = new day7();
        System.out.println(myday.find("a"));

    }
}