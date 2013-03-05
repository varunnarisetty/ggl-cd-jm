package com.codejam.waterheds;

import java.util.ArrayList;

import com.codejam.util.InputReaderClass;

public class MainClass {

	private static int testCaseNumber;
	private static int beginLine = 1;
	private static int endLine = 0;
	private static int counter = 1;
	private static String[] arr = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}; 
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		
		if(args.length !=0){
			
			InputReaderClass reader = new InputReaderClass(args[0]) {
				int width = 0;
				int height = 0;
				int[][] mapMatrix;
				
				@Override
				public void readLine(int lineNumber, String lineStr) {
					
					if(lineNumber == 0){
						testCaseNumber = Integer.parseInt(lineStr.trim());
					}else if(lineNumber == beginLine){
						String[] temp = lineStr.split(" ");
						width = Integer.parseInt(temp[1]);
						height = Integer.parseInt(temp[0]);
						beginLine = lineNumber;
						endLine = endLine + height+1;
						mapMatrix = new int[height][width];
					}else if(lineNumber == endLine){
						String[] temp = lineStr.split(" ");
						for(int i =0;i<temp.length;i++){
							mapMatrix[lineNumber-beginLine -1][i] = Integer.parseInt(temp[i]);
						}
						beginLine = endLine +1;
						printResultMatrix(mapMatrix,width,height);
					}else{
						String[] temp = lineStr.split(" ");
						for(int i =0;i<temp.length;i++){
							mapMatrix[lineNumber-beginLine -1][i] = Integer.parseInt(temp[i]);
						}
					}
					
				}

				private void printResultMatrix(int[][] mapMatrix2, int width2,
						int height2) {
				System.out.println("Case #"+counter+":");
				MyInteger[][] target = new MyInteger[height2][width2];
				int basin = 0;
				for(int i =0; i< height2;i++){
					for(int j=0;j< width2;j++){
						target[i][j] = new MyInteger(-1);
					}
				}
				
				
				for(int i =0; i< height2;i++){
					for(int j=0;j< width2;j++){
						int top = 10001;
						int left = 10001;
						int right = 10001;
						int bottom = 10001;
						if(i > 0){
							top = mapMatrix2[i -1][j];
						}
						if(i < height2-1){
							bottom = mapMatrix2[i+1][j];
						}
						if(j >0){
							left = mapMatrix2[i][j-1];
						}
						if(j < width2 -1){
							right = mapMatrix2[i][j+1];
						}
						int min = getMin(top,left,right,bottom,mapMatrix2[i][j]);
						if(min ==5){
							target[i][j].setInt(basin);
							target[i][j].setVal(arr[basin]);
							basin++;
						}
						
						
						/*switch(min){
						case 1:
							target[i][j] = target[i-1][j];
							break;
						case 2:
							target[i][j] = target[i][j-1];
							break;
						case 3:
							target[i][j+1] = target[i][j]; 
							break;
						case 4:
							target[i+1][j] = target[i][j];
							break;
						case 5:
							target[i][j].setInt(basin);
							basin++;
							break;
						}*/
						
						//System.out.print(mapMatrix2[i][j]+" ");
					}
				//	System.out.println("");
			}
				
				for(int i =0; i< height2;i++){
					for(int j=0;j< width2;j++){
						
						if(target[i][j].getInt() == -1){
							ArrayList<MyInteger> list = new ArrayList<MyInteger>();
							MyInteger myInt = updateList(list,target,mapMatrix2,i,j,height2,width2);
							for(int k =0;k<list.size();k++){
								list.get(k).setInt(myInt.getInt());
								list.get(k).setVal(myInt.getVal());
							}
						}
					}
				}
				
				for(int i =0; i< height2;i++){
						for(int j=0;j< width2;j++){
							System.out.print(target[i][j].getVal()+" ");
						}
						System.out.println("");
				}
				counter++;
				}

				private MyInteger updateList(ArrayList<MyInteger> list, MyInteger[][] target,int[][] mapMatrix2, int i,
						int j, int height2, int width2) {
					if(target[i][j].getInt() != -1){
						return target[i][j];
					}else{
						int top = 10001;
						int left = 10001;
						int right = 10001;
						int bottom = 10001;
						if(i > 0){
							top = mapMatrix2[i -1][j];
						}
						if(i < height2-1){
							bottom = mapMatrix2[i+1][j];
						}
						if(j >0){
							left = mapMatrix2[i][j-1];
						}
						if(j < width2 -1){
							right = mapMatrix2[i][j+1];
						}
						int min = getMin(top,left,right,bottom,mapMatrix2[i][j]);
						int p,q;
						switch(min){
						case 1:
							 p = i -1;
							 q = j;
							list.add(target[i][j]);
							
							return updateList(list, target, mapMatrix2, p, q, height2, width2);
						case 2:
							p = i;
							q = j-1;
							list.add(target[i][j]);
							
							return updateList(list, target, mapMatrix2, p, q, height2, width2);
						case 3:
							p = i;
							q = j+1;
							list.add(target[i][j]);
							
							return updateList(list, target, mapMatrix2, p, q, height2, width2);
						case 4:
							p = i +1;
							q = j;
							list.add(target[i][j]);
							
							return updateList(list, target, mapMatrix2, p, q, height2, width2);
						default:
							return target[i][j];
						}
					}
					//return null;
				}

				private int getMin(int top, int left, int right, int bottom,
						int i) {
					if(i != -1){
						
						if(i<= top && i<=left && i <=right && i<= bottom ){
							
							return 5;
						}
						
						if(top <= left && top <= right && top<= bottom){
							
							return 1;
						}
						if(left <= right && left<=bottom){
							return 2;
						}
						if(right<= bottom){
							return 3;
						}else{
							return 4;
						}
					}else{
						return 0;
					}
					
				}

				@Override
				public void onFinishReading() {
					// TODO Auto-generated method stub
					
				}
				
			};
			reader.readFile();
				
			
		}else{
			System.out.println("please pass input file name");
		}
		long end = System.currentTimeMillis();
		
		System.out.println("Total time taken is"+(end-start));
	}
	
	

}
