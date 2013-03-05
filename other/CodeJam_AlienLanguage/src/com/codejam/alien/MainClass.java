package com.codejam.alien;

public class MainClass {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
	InputReaderClass inputReader = new InputReaderClass(args[0]);
	InputBean inputBean = null;
	try {
		inputBean = inputReader.readFile();
	} catch (Exception e) {
		
		e.printStackTrace();
	}
	
	if(inputBean !=null){
		int size = inputBean.getTestCaseSize();
		
		for(int i =0;i<size;i++){
			
			int dictionarySize = inputBean.getWordDictionaryList().size();
			int count =0;
			String pattern = inputBean.getTestCaseList().get(i);
			Finder finder = new Finder();
			finder.setPattern(pattern);
				for(int j=0;j<dictionarySize;j++){
					boolean flag = finder.matchWord(inputBean.getWordDictionaryList().get(j));
					if(flag){
						count++;
					}
				}
				System.out.println("Output #"+(i+1)+": "+count);
		}
		
	}else{
		System.out.println("error in input file");
	}

	}

	
}
