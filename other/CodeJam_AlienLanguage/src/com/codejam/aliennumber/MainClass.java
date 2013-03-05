package com.codejam.aliennumber;

import com.codejam.util.InputReaderClass;

public class MainClass {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		InputReaderClass reader = new InputReaderClass(args[0]) {
			
			@Override
			public void readLine(int lineNumber, String lineStr) {
				if(lineNumber == 0){
					
				}else{
					
					InputBean input = getInputBean(lineStr);
					String result = getResult(input);
					System.out.println("Case #"+lineNumber+": "+result);
					
				}
				
			}
			
			private InputBean getInputBean(String lineStr){
				InputBean input = new InputBean();
				String[] lineArr = lineStr.split(" ");
				
					input.setSrcNumber(lineArr[0]);
					for(int i =0 ;i<lineArr[1].length();i++){
						String key = lineArr[1].charAt(i)+"";
						Integer value = new Integer(i);
						input.getSrcNumberSystem().put(key, value);
					}
					input.setSrcDigitLength(lineArr[1].length());
					for(int i =0 ;i<lineArr[2].length();i++){
						String value = lineArr[2].charAt(i)+"";
						Integer key = new Integer(i);
						input.getTargetNumberSystem().put(key, value);
					}
					input.setTargetDigitLength(lineArr[2].length());
				return input;
			}
			private String getResult(InputBean input) {
				int value = getDesimalValue(input);
				String result = targetNumber(value,input);
				return result;
			}

			private String targetNumber(int value,InputBean input) {
				String targetNumber = "";
				int len = input.getTargetDigitLength();
				while(value >= len){
					int unit = value%len;
					value = value/len;
					String temp = input.getTargetNumberSystem().get(unit);
					targetNumber = temp + targetNumber;
				}
				int unit = value%len;
				value = value/len;
				String temp = input.getTargetNumberSystem().get(unit);
				targetNumber = temp + targetNumber;
				
				return targetNumber;
			}

			private int getDesimalValue(InputBean input) {
				int size = input.getSrcDigitLength();
				int desimal = 0;
				String srcNumber = input.getSrcNumber();
				for(int i =0;i<srcNumber.length();i++){
					Integer unit = input.getSrcNumberSystem().get(srcNumber.charAt(srcNumber.length() - (i+1))+"");
					desimal = desimal +unit*(int) Math.pow(input.getSrcDigitLength(), i);
				}
				return desimal;
			}

			@Override
			public void onFinishReading() {
				// TODO Auto-generated method stub
				
			}
		};
		
		reader.readFile();
		
		long end = System.currentTimeMillis();
		
		System.out.println("Total time taken is"+(end-start));
	}

}
