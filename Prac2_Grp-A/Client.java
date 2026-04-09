import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        try {
            // Connect to registry
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            // Lookup remote object
            StringService stub = (StringService) registry.lookup("StringService");

            // Input strings
            String str1 = "Hello ";
            String str2 = "World";

            // Remote call
            String result = stub.concatenate(str1, str2);

            // Output
            System.out.println("Concatenated String: " + result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}