/**
 * Creates a LinkedList that stores nodes of objects
 * @author SadiqSarwar
 *
 */
public class LinkedList{
	
	/**
	 * Node class that creates a node for the LinkedList class
	 * @author SadiqSarwar
	 */
	private static class Node{
		/** Object information */
		private Contact data;
		/** Next node within the list */
		private Node next;
		
		/**
		 * Constructs the node
		 * @param c contact object
		 */
		public Node(Contact c){
			data = c;
			next = null;
		}
		
		/**
		 * Constructs the node with passed in parameters
		 * @param c contact object
		 * @param n node parameter
		 */
		public Node (Contact c, Node n){
			data = c;
			next = n;
		}
		
		/**
		 * LinkedList returned in string information
		 * @return data information of object
		 */
		@Override
		public String toString(){
			return data.toString();
		}
			
	} // End of Node class
	
	/** First Node in LinkedList */
	private Node first;
	/** Last Node in LinkedList */
	private Node last;
	
	/** 
	 * Checks to see if the LinkedList is empty 
	 * @return t/f if depending on condition
	 */
	public boolean isEmpty(){
		return first == null;
	}
	
	/**
	 * Checks the size of the Linked List
	 * @return the size of the List
	 */
	public int size(){
		int count = 0;
		Node n = first;
		while (n != null){
			count++;
			n = n.next;
		}
		return count;
	}
	
	/**
	 * Gets a specific contact data
	 * @param i index of list
	 * @return contact object data
	 */
	public Contact get(int i){
		if (i < 0 || i >= size()){
			System.out.println("[Index Out of Bounds]");
			return null;
		}else{
			Node n = first;
			for (int j = 1; j <= i; j++){
				n = n.next;
			}
			return n.data;
		}
	}
	
	/**
	 * Sets a contact object equal to a another
	 * @param i index of list
	 * @param c contact object
	 */
	public void set (int i, Contact c){
		if (i < 0 || i >= size()){
			System.out.println("[Index Out of Bounds]");
		}else{
			Node n = first;
			for (int j = 1; j <= i; j++){
				n = n.next;
			}
			n.data = c;
		}
	}
	
	/**
	 * Creates a label for each object
	 * @return The object displayed as a string
	 */
	@Override
	public String toString(){
		String str = "";
		Node n = first;
		while(n != null){
			str = str + n.data + "\n";
			n = n.next;
		}
		return str;
	}
	
	/**
	 * Adds a contact object within the Linked List
	 * @param c passed in contact object
	 */
	public void add (Contact c){
		if(isEmpty()){
			first = new Node (c);
			last = first;
		}else{
			Node n = new Node (c);
			last.next = n;
			last = n;
		}
	}
	
	/**
	 * Removes a contact object from the LinkedList
	 * @param i index of Linked List
	 * @return removed data of contact object
	 */
	public String remove (int i){
		String rem = "";
		if(i < 0 || i >= size()){
			System.out.println("[Index Out of Bounds]");
		} else {
			if(i == 0){
				rem = first.data.toString();
				first = first.next;
				if(first == null){
					last = null;
				}
			} else {
				Node n = first;
				for(int j = 1; j < i; j++){
					n = n.next;
				}
				rem = n.next.data.toString();
				n.next = n.next.next;
				if(n.next == null){
					last = n;
				}
			}
		}
		return rem;
	}
	
	/**
	 * Checks for contacts with same last name
	 * @param s last name parameter
	 */
	public void searchN (String s){
		int count = 0;
		Node n = first;
		for(int i = 0; i < size(); i++){
			if (n.data.checkLN(s)){
				count++;
				System.out.println(n.data);
			}
			n = n.next;
		}
		if(count == 0){
			System.out.println("[Contact Not Found]");
			System.out.println();
		}
	}
	
	/**
	 * Checks for contacts with same zip code
	 * @param s zipcode parameter
	 */
	public void searchZC (String s){
		int count = 0;
		Node n = first;
		for(int i = 0; i < size(); i++){
			if (n.data.checkZC(s)){
				count++;
				System.out.println(n.data);
			}
			n = n.next;
		}
		if(count == 0){
			System.out.println("[Contact Not Found]");
			System.out.println();
		}
	}
	
}
