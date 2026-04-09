import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) {
        try {
            // Create object
            StringServiceImpl obj = new StringServiceImpl();

            // Create registry on port 1099
            Registry registry = LocateRegistry.createRegistry(1099);

            // Bind object
            registry.rebind("StringService", obj);

            System.out.println("Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}