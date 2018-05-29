import org.apache.http.HttpHost;
import org.apache.http.HttpResponse;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

/**
 * A simple example of HTTP basic access authentication.
 *
 * @author A cool InfoJobs dev ;)
 */
public class BasicAuthenticationExample {

    public static void main(String[] args) throws Exception {

        DefaultHttpClient client = new DefaultHttpClient();

        HttpHost targetHost = new HttpHost("api.infojobs.net", 443, "https");

        // Provide the credentials to be used for the host against which
        // authentication is to be attempted.
        client.getCredentialsProvider().setCredentials(
            new AuthScope(targetHost.getHostName(), targetHost.getPort()),
            new UsernamePasswordCredentials("cbbb268e3ae74f2b833efcf354c8eb62", "zUvMo29uTptnuw7mUTZ1OXnPSHEWnjCM9KG/JKWXK1CHl9Y2HB")
        );

        // create a GET method that queries some API operation
        HttpGet request = new HttpGet("/api/1/offer");

        try {
            // execute the operation
            HttpResponse response = client.execute(targetHost, request);

            // print the status and the contents of the response
            System.out.println(response.getStatusLine());
            System.out.println(EntityUtils.toString(response.getEntity()));
        } finally {
            // release any connection resources used by the method
            client.getConnectionManager().shutdown();
        }
    }
}
