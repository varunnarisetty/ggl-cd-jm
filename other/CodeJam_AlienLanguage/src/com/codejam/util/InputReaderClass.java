package com.codejam.util;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public abstract class InputReaderClass {

	private String filePath;
	public InputReaderClass(String filePath){
		
		this.filePath = filePath;
		
	}
	
	public void readFile()  {

		

		Scanner scan = null;
		try {
			scan = new Scanner(new File(filePath));
		} catch (FileNotFoundException e) {
			
			e.printStackTrace();
		}

		for(int i=0;scan.hasNext();i++){
			String line = null;
			line = scan.nextLine();
			readLine(i, line);
			
			
		}
		
		onFinishReading();

		
	}
	
	public abstract void readLine(int lineNumber,String lineStr);
	
	public abstract void onFinishReading();
	
}
