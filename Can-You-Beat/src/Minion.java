public class Minion {
	private int atk;
	private int atkchc;
	private int hel;
	private int maxhel;
	private boolean ally;
	private String name;
	
	public Minion(String name, int atk, int maxhel, int hel, boolean ally)
	{
		this.name = name;
		
		if (atk < 0) atk = 0;
		this.atk = atk;
		
		if (ally) atkchc = 1;
		else atkchc = 0;
		
		if (hel < 1) hel = 1;
		this.hel = hel;

		if (maxhel < hel) maxhel = hel;
		this.maxhel = hel;
		
		this.ally = ally;
	}
}
