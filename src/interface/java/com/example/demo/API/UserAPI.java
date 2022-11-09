package com.example.demo.API;
import com.example.demo.model.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import java.net.URLConnection;


public class UserAPI {

	/**
	 *
	 * param body:should be name1=value1&name2=value2
	 */
	public static String login(String url, String email,String password) {
		PrintWriter out = null;
		BufferedReader in = null;
		String result = "";
		try {
			URL realUrl = new URL(url);
			URLConnection conn = realUrl.openConnection();
			conn.setRequestProperty("accept", "*/*");
			conn.setRequestProperty("connection", "Keep-Alive");
			conn.setRequestProperty("user-agent",
					"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)");
			conn.setDoOutput(true);
			conn.setDoInput(true);
			out = new PrintWriter(conn.getOutputStream());
			String param = "email=" + email + "&password=" + password;
			out.print(param);
			out.flush();
			in = new BufferedReader(
					new InputStreamReader(conn.getInputStream()));
			String line;
			while ((line = in.readLine()) != null) {
				result += line;
			}
		} catch (Exception e) {
			System.out.println("Unable to send the request" + e);
			e.printStackTrace();
		}
		finally {
			try {
				if (out != null) {
					out.close();
				}
				if (in != null) {
					in.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		System.out.println(result);
		//User user = new User(id,token);
		User user = new User("13","c83e4456ca2b14cd54ccbb96074169e7f46e34d8");
		return result;
	}



	/*
	public static void main(String[] args){
		//login("http://127.0.0.1:8000/api/v1/login/","email=test@gmail.com&password=test123456");
		login("http://127.0.0.1:8000/api/v1/login/","test@gmail.com","test123456");
	}
	*/

}

