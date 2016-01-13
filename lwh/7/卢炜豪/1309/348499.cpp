import java.io.*;
import java.text.StringCharacterIterator;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		String s;
		Scanner in = new Scanner(System.in);
		while(in.hasNextLine()) {
			s = in.next();
			Stack sta = new Stack();
			int sLength = s.length();
			for(int i=0;i<sLength;i++){
				char c = s.charAt(i);
				//System.out.println("c="+c);
				if(sta.empty()) {
					sta.push(c);
				}
				else {
					char cc = (char)sta.peek();
					sta.push(c);
					int ic = (int)c;
					int icc= (int)cc;
					//System.out.println("top1="+(char)sta.peek());
					if(ic==icc-1||ic==icc+1||ic==icc-2||ic==icc+2) {
						//System.out.println("pophere");
						if(!sta.empty())
						sta.pop();
						//System.out.println("@pophere");
						if(!sta.empty())
						sta.pop();
					}
					//if(!sta.empty())
					//System.out.println("top2="+(char)sta.peek());
				}
			}
			if(sta.isEmpty()) {
				System.out.println("YES");
			}
			else
				System.out.println("NO");
		}
	}

}
