package com.codejam.alien;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Finder {

	private Pattern pattern;
	
	public void setPattern(String patternString){
		
		patternString = patternString.replace('(', '[');
		patternString = patternString.replace(')', ']');
		pattern = Pattern.compile(patternString);
	}
	public boolean matchWord(String word){
		
		Matcher match = pattern.matcher(word);
		return match.matches();
	}
	
	
}
