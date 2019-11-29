public class Field {
   
   private Minion[] ally;
   private Minion[] enemy;
   private int ally_minion;
   private int enemy_minion;
   private int mode;
   
   public Field(int difficulty, int mode)
   {
	   // 난이도와 모드에 따라 하수인의 개수와 종료 조건 변경
   }
   
   public boolean attack(String name_of_ally, String name_of_enemy)
   {
      boolean ok_ally = false, ok_enemy = false;
      int i, j;
      
      for (i = 0 ; i < ally_minion ; i++)
      {
         if (ally[i].getName().equals(name_of_ally) && ally[i].canAttack())
         {
            ok_ally = true;
            break;
         }
      }
      
      for (j = 0 ; j < enemy_minion ; j++)
      {
         if (enemy[j].getName().equals(name_of_enemy))
         {
            ok_enemy = true;
            break;
         }
      }
      
      if (ok_ally && ok_enemy) ally[i].attack(enemy[j]);
      else return false;
      
      return true;
   }

   public void minionDead(Minion dead_minion, boolean isAlly) 
   {
	  if (isAlly)
	  {
		  int i;
		  for (i = 0 ; i < ally_minion ; i++) if (ally[i] == dead_minion) break;
		  for (int j = i ; j < ally_minion ; j++)
		  {
			  if (j < ally_minion-1) ally[j] = ally[j+1];
			  else ally[j] = null;
		  }
		  ally_minion--;
	  }
	  else
	  {
		  int i;
		  for (i = 0 ; i < enemy_minion ; i++) if (enemy[i] == dead_minion) break;
		  for (int j = i ; j < enemy_minion ; j++)
		  {
			  if (j < enemy_minion-1) enemy[j] = enemy[j+1];  
			  else enemy[j] = null;
		  }
		  ally_minion--;
	  }
	  dead_minion.i_am_dead();
	  for (int j = 0 ; j < ally_minion ; j++) ally[j].somebody_dead(dead_minion);
	  for (int j = 0 ; j < enemy_minion ; j++) enemy[j].somebody_dead(dead_minion);
   }
}