/**
 * Contact class that creates an object for each contact
 */
public class Contact {
	
	/** The first name of the contact */
	private String fName; 
	/** The last name of the contact */
	private String lName; 
	/** The phone number of the contact */
	private String pNum;	
	/** The address of the contact */
	private String address;
	/** The city of the contact */
	private String city;
	/** The zip code of the contact */
	private String zCode;
	
	/**
	 * Constructs the the contact object variables
	 * @param fNameP first name of the contact
	 * @param lNameP last name of the contact
	 * @param pNumP phone number of the contact
	 * @param addressP address of the contact
	 * @param cityP city of the contact
	 * @param zCodeP zip code of the contact
	 */
	public Contact(String fNameP, String lNameP, String pNumP, String addressP, String cityP, String zCodeP){
		fName = fNameP;
		lName = lNameP;
		pNum = pNumP;
		address = addressP;
		city = cityP;
		zCode = zCodeP;
	}
	
	/**
	 * Creates a label for each object
	 * @return The variables of each object displayed as a string
	 */
	@Override
	public String toString(){
		return (fName + "," + lName + "," + pNum + "," + address +"," + city + "," + zCode);
	}
	
	/**
	 * Compares each contact last name and first name
	 * @param c the given contact
	 * @return integer of compared value
	 */
	public int compareTo(Contact c){
		if(this.lName.equals(c.lName)){
			return(this.fName.compareTo(c.fName));
		}else{
			return(this.lName.compareTo(c.lName));
		}
	}
	
	/**
	 * Checks to see if two contacts are equal
	 * @param o passed in explicit object
	 * @return t/f depending upon condition
	 */
	@Override
	public boolean equals(Object o){
		if(o instanceof Contact){
			Contact c = (Contact) o;
			return (this.fName.equals(c.fName) && this.lName.equals(c.lName) && this.pNum.equals(c.pNum) && this.address.equals(c.address) && this.city.equals(c.city) && this.zCode.equals(c.zCode));
		}
		return false;
	}
	
	/**
	 * Checks to see if the last names are equal
	 * @param s last name
	 * @return t/f if the given string is equal to the object variable
	 */
	public boolean checkLN(String s){
		if(this.lName.equals(s)){
			return true;
		}else{
			return false;
		}
	}
	
	/**
	 * Checks to see if the zip codes are equal
	 * @param s zip code
	 * @return t/f if the given string is equal to the object variable
	 */
	public boolean checkZC(String s){
		if(this.zCode.equals(s)){
			return true;
		}else{
			return false;
		}
	}
	
	/**
	 * Checks to see if the first and last names are equal
	 * @param fN first name
	 * @param lN last name
	 * @return t/f if the given string is equal to the object variable
	 */
	public boolean checkFLN(String fN, String lN){
		if(this.fName.equals(fN) && this.lName.equals(lN)){
			return true;
		}else{
			return false;
		}
	}
	
	/**
	 * Sets the first name equal to the given string
	 * @param s new first name of contact
	 */
	public void changeFN(String s){
		fName = s;
	}
	
	/**
	 * Sets the last name equal to the given string
	 * @param s new last name of contact
	 */
	public void changeLN(String s){
		lName = s;
	}
	
	/**
	 * Sets the phone number equal to the given string
	 * @param s new phone number of contact
	 */
	public void changePN(String s){
		pNum = s;
	}
	
	/**
	 * Sets the address equal to the given string
	 * @param s  new address of contact
	 */
	public void changeAddress(String s){
		address = s;
	}
	
	/**
	 * Sets the city equal to the given string
	 * @param s new city of contact
	 */
	public void changeCity(String s){
		city = s;
	}
	
	/**
	 * Sets the zip code equal to the given string
	 * @param s new zip code of contact
	 */
	public void changeZC(String s){
		zCode = s;
	}
}
