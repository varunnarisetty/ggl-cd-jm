package com.codejam.waterheds;

public class MyInteger{
	private int i;
	private String val;
	public MyInteger(int i) {
		this.i = i ;
		val = "$";
	}
	
	public int getInt(){
		return i;
	}
	
	public void setInt(int i){
		this.i = i;
	}

	public String getVal() {
		return val;
	}

	public void setVal(String val) {
		this.val = val;
	}
}