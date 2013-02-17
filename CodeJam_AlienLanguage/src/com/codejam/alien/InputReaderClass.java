package com.codejam.alien;

import java.io.File;
import java.util.Scanner;

public class InputReaderClass {

	private String filePath;
	public InputReaderClass(String filePath){
		
		this.filePath = filePath;
	}
	
	public InputBean readFile() throws Exception {

		InputBean inputBean = new InputBean();

		Scanner scan = new Scanner(new File(filePath));

		for(int i=0;scan.hasNext();i++){
			String line = null;
			if(i == 0){
				line = scan.nextLine();
				String[] firstLine = line.split(" ");
				inputBean.setWordSize(Integer.parseInt(firstLine[0]));
				inputBean.setDictionarySize(Integer.parseInt(firstLine[1]));
				inputBean.setTestCaseSize(Integer.parseInt(firstLine[2]));
			}else if(i <= inputBean.getDictionarySize()){
				line = scan.nextLine();
				inputBean.getWordDictionaryList().add(line);
			}else{
				line = scan.nextLine();
				
				//line.replace("(", "[");
				
				/*String[] arr = line.split("(");
				StringBuffer buff = new StringBuffer();
				for(int k=0;k<arr.length;k++){
					buff.append(buff);
				}*/
				
				/*line.replaceAll("(", "[");
				line.replaceAll(")", "]");*/
				inputBean.getTestCaseList().add(line);
			}
		}

		return inputBean;
	}
	
	
}
