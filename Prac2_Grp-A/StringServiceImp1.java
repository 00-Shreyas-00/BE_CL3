import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class StringServiceImpl extends UnicastRemoteObject implements StringService {

    protected StringServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}