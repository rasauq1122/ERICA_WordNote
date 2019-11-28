public class Minion {
   private int atk;
   private int atkchc;
   private int hel;
   private int maxhel;
   private boolean ally;
   private String name;
   private Field myfield;
   
   public Minion(String name, int atk, int maxhel, int hel, boolean ally, Field myfield)
   {
      this.name = name;
      
      if (atk < 0) atk = 0;
      this.atk = atk;
      
      if (ally) atkchc = 1;
      else atkchc = 1;
      
      if (hel < 1) hel = 1;
      this.hel = hel;

      if (maxhel < hel) maxhel = hel;
      this.maxhel = hel;
      
      this.ally = ally;
      
      this.myfield = myfield;
   }
   
   public String getName() {return this.name;}
   
   public boolean canAttack() {return atkchc > 0;}
   
   public int getAttack() {return atk;}
   
   public void getDamage(int damage, Minion other)
   {
      hel -= other.getAttack();
      if (hel <= 0) myfield.minionDead(this,ally);
   }
   
   public void attack(Minion other)
   {
      atkchc--;
      other.getDamage(this.getAttack(), this);
      this.getDamage(other.getAttack(), other);
   }
}