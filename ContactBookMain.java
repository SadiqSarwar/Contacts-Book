/**
 * Sadiq Sarwar
 * November 6, 2017
 * Project#3 - Creates a contact book that can be modified through LinkedList
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.ArrayList;

public class ContactBookMain {

	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		LinkedList contactList = new LinkedList ();
		
		boolean testInputRead = true;
		while (testInputRead){
			try{
				Scanner read = new Scanner (new File("addresses.txt"));
				while(read.hasNext()){ 
					String fileLine = read.nextLine();
					Contact c = contactImporter(fileLine);
					contactList.add(c);

				} // while(Read.hasNextInt())
				testInputRead = false;
			} // try --> while (TestInputRead)
			catch(FileNotFoundException e){
				System.out.println("Error - File Not Found");
			} // catch(FileNotFoundException e)
		} // while (TestInputRead)	
		
		int option = -1;
		while (option != 0){
			System.out.println("[Menu]");
			System.out.println("1 - Add New Contact");
			System.out.println("2 - Remove Contact");
			System.out.println("3 - Search for Contact");
			System.out.println("4 - Update Contact Information");
			System.out.println("5 - Total Number of Contacts");
			System.out.println("6 - View All Contacts");
			System.out.println("0 - Quit");
			System.out.print("Option: ");
			option = CheckInput.checkIntRange(0, 6);
			System.out.println();
			
			if(option == 1){
				contactList = sort(contactList);
				contactAdder(contactList);
			}
			else if(option == 2){
				contactList = sort(contactList);
				contactRemover(contactList);
			}
			else if(option == 3){
				contactList = sort(contactList);
				search(contactList);
			}
			else if(option == 4){
				contactList = sort(contactList);
				updateContact(contactList);
			}
			else if(option == 5){
				contactList = sort(contactList);
				System.out.println("[Total Number of Contacts]");
				System.out.println("Contacts: " + contactList.size());
				System.out.println();
			}
			else if(option == 6){
				contactList = sort(contactList);
				System.out.println("[Contacts]");
				System.out.println(contactList.toString());
			}
			else if(option == 0){
				export(contactList);
				System.out.println("[Program Will Now Exit]");
			}
			
		}
	} // End of main method
	
	/**
	 * Imports a given file and saves it as a contact object
	 * @param contact object containing imported information
	 * @return newly constructed contact
	 */
	public static Contact contactImporter(String contact){
		String [] indivL = contact.split(",");
		Contact cont = new Contact(indivL[0],indivL[1],indivL[2],indivL[3],indivL[4],indivL[5]);
		return cont;
	}
	
	/**
	 * Adds a contact into the Linked List
	 * @param contactList LinkedList of contact objects
	 * @return contactList with contact objects
	 */
	public static LinkedList contactAdder(LinkedList contactList){
		System.out.print("First Name: ");
		String fName = CheckInput.getString();
		System.out.print("Last Name: ");
		String lName = CheckInput.getString();
		System.out.print("Phone Number: ");
		String pNum = CheckInput.getString();
		System.out.print("Address: ");
		String address = CheckInput.getString();
		System.out.print("City: ");
		String city = CheckInput.getString();
		System.out.print("Zip Code: ");
		String zCode = CheckInput.getString();
		Contact cont = new Contact(fName,lName,pNum,address,city,zCode);
		contactList.add(cont);
		sort(contactList);
		System.out.println();
		return contactList;
	}
	
	/**
	 * Removes contact object from a Linked List
	 * @param contactList LinkedList of contact objects
	 * @return contactList with contact objects
	 */
	public static LinkedList contactRemover(LinkedList contactList){
		System.out.println("[Options]");
		System.out.println("1 - Remove through list index");
		System.out.println("2 - Remove through first and last name");
		System.out.print("Option: ");
		int choice = CheckInput.checkIntRange(1,2);
		if (choice == 1){
			System.out.print("Index: ");
			int index = CheckInput.checkIntRange(0, contactList.size());
			contactList.remove(index);
			System.out.print("[Contact Removed]");
			System.out.println();
			
		}else if (choice ==2){
			System.out.print("First Name: ");
			String fName = CheckInput.getString();
			System.out.print("Last Name: ");
			String lName = CheckInput.getString();
			boolean found = false;
			for(int i=0; i < contactList.size(); i++){
				if(contactList.get(i).checkFLN(fName, lName)){
					contactList.remove(i);
					System.out.println("[Contact Removed]");
					found = true;
					System.out.println();
				}
			}
			if(!found){
				System.out.println("[Contact Not Found]");
				System.out.println();
			}
		}
		return contactList;
	}
	
	/**
	 * Searches for a contact from LinkedList
	 * @param contactList LinkedList of contact objects
	 * @return contactList with contact objects
	 */
	public static LinkedList search(LinkedList contactList){
		System.out.println("[Options]");
		System.out.println("1 - Search by last name");
		System.out.println("2 - Search by zip code");
		System.out.print("Option: ");
		int choice = CheckInput.checkIntRange(1, 2);
		if (choice == 1){
			System.out.print("Last Name: ");
			String lName = CheckInput.getString();
			contactList.searchN(lName);
			System.out.println();
			
		}else if (choice ==2){
			System.out.print("Zip Code: ");
			String zCode = CheckInput.getString();
			contactList.searchZC(zCode);
			System.out.println();
		}
		return contactList;
	}
	
	/**
	 * Sorts the contact information within a LinkedList
	 @param contactList LinkedList of contact objects
	 * @return contactList with contact objects
	 */
	public static LinkedList sort(LinkedList contactList){
		for(int i = 0; i < contactList.size(); i++){
			int lowest = i;
			for(int j = i + 1; j < contactList.size(); j++){
				if(contactList.get(j).compareTo(contactList.get(lowest)) < 0){
					lowest = j;
					
				}
			}
			Contact swap = contactList.get(i);
			contactList.set(i, contactList.get(lowest));
			contactList.set(lowest, swap);
		}
		return contactList;
	}
	
	/**
	 * Exports the Linked List into a designated file
	 * @param contactList LinkedList of contact objects
	 */
	public static void export(LinkedList contactList){
		try{
			PrintWriter writer = new PrintWriter("addresses.txt");
			for(int i = 0; i < contactList.size(); i++){
				writer.println(contactList.get(i));
			}
			writer.close();
		}catch (FileNotFoundException fnf){
			System.out.println("[File Not Found]");
		}
	}
	
	/**
	 * Updates contact information of a given contact object
	 * @param contactList LinkedList of contact objects
	 * @return contactList with contact objects
	 */
	public static LinkedList updateContact(LinkedList contactList){
		for(int i = 0; i < contactList.size(); i++){
			System.out.println((i+1) + " - " + contactList.get(i));
		}
		System.out.print("Choice: ");
		int choice = CheckInput.checkIntRange(0, contactList.size());
		System.out.println("Accessing Contact: " + contactList.get(choice-1));
		System.out.println("1. First Name");
		System.out.println("2. Last Name");
		System.out.println("3. Phone Number");
		System.out.println("4. Address");
		System.out.println("5. City");
		System.out.println("6. Zip Code");
		System.out.print("Modify: ");
		int modify = CheckInput.checkIntRange(1,6);
		if(modify == 1){
			System.out.print("New First Name: ");
			String fName = CheckInput.getString();
			contactList.get(choice-1).changeFN(fName);
		} else if(modify == 2){
			System.out.print("New Last Name: ");
			String lName = CheckInput.getString();
			contactList.get(choice-1).changeLN(lName);
		} else if(modify == 3){
			System.out.print("New Phone Number: ");
			String pNum = CheckInput.getString();
			contactList.get(choice-1).changePN(pNum);
		} else if(modify == 4){
			System.out.print("New Address: ");
			String address = CheckInput.getString();
			contactList.get(choice-1).changeAddress(address);
		} else if(modify == 5){
			System.out.print("New City: ");
			String city = CheckInput.getString();
			contactList.get(choice-1).changeCity(city);
		} else if(modify == 6){
			System.out.print("New Zip Code: ");
			String zCode = CheckInput.getString();
			contactList.get(choice-1).changeZC(zCode);
		}
		System.out.println("[Contact Has Been Modified]");
		System.out.println();
		return contactList;
	}
	

}
