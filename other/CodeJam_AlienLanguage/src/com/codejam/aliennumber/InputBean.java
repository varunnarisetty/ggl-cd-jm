package com.codejam.aliennumber;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class InputBean {

	private HashMap<Integer, String> targetNumberSystem = new HashMap<Integer, String>();
	private HashMap<String, Integer> srcNumberSystem = new HashMap<String, Integer>();
	private int srcDigitLength;
	private int targetDigitLength;
	private String srcNumber;
	
	
	public InputBean(){
		
		
	}


	public HashMap<Integer, String> getTargetNumberSystem() {
		return targetNumberSystem;
	}


	public void setTargetNumberSystem(HashMap<Integer, String> targetNumberSystem) {
		this.targetNumberSystem = targetNumberSystem;
	}


	public HashMap<String, Integer> getSrcNumberSystem() {
		return srcNumberSystem;
	}


	public void setSrcNumberSystem(HashMap<String, Integer> srcNumberSystem) {
		this.srcNumberSystem = srcNumberSystem;
	}


	public int getSrcDigitLength() {
		return srcDigitLength;
	}


	public void setSrcDigitLength(int srcDigitLength) {
		this.srcDigitLength = srcDigitLength;
	}


	public int getTargetDigitLength() {
		return targetDigitLength;
	}


	public void setTargetDigitLength(int targetDigitLength) {
		this.targetDigitLength = targetDigitLength;
	}


	public String getSrcNumber() {
		return srcNumber;
	}


	public void setSrcNumber(String srcNumber) {
		this.srcNumber = srcNumber;
	}

	
	
	
}
