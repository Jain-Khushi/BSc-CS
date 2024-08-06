import java.io.*;

 class Copy {

    public static void main(String[] args) {

        try {
            FileReader fr = new FileReader("FIRST.txt");
            BufferedReader br = new BufferedReader(fr);
            FileWriter fw = new FileWriter("SECOND.txt", true);
            String s;

            while ((s = br.readLine()) != null) {
                fw.write(s);
                fw.flush();
            }
            br.close();
            fw.close();
            System.out.println("file copied");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
