package com.codejam.alien;

import java.util.ArrayList;

public class InputBean {

	private ArrayList<String> wordDictionaryList;
	private ArrayList<String> testCaseList;
	private int wordSize;
	private int dictionarySize;
	private int testCaseSize;
	
	public InputBean(){
		
		wordDictionaryList = new ArrayList<String>();
		testCaseList = new ArrayList<String>();
	}

	public ArrayList<String> getWordDictionaryList() {
		return wordDictionaryList;
	}

	public void setWordDictionaryList(ArrayList<String> wordDictionaryList) {
		this.wordDictionaryList = wordDictionaryList;
	}

	public ArrayList<String> getTestCaseList() {
		return testCaseList;
	}

	public void setTestCaseList(ArrayList<String> testCaseList) {
		this.testCaseList = testCaseList;
	}

	public int getWordSize() {
		return wordSize;
	}

	public void setWordSize(int wordSize) {
		this.wordSize = wordSize;
	}

	public int getDictionarySize() {
		return dictionarySize;
	}

	public void setDictionarySize(int dictionarySize) {
		this.dictionarySize = dictionarySize;
	}

	public int getTestCaseSize() {
		return testCaseSize;
	}

	public void setTestCaseSize(int testCaseSize) {
		this.testCaseSize = testCaseSize;
	}
	
	
	
}
