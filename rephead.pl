$counter = 0;
while(<>){
   if(/>scaff.+/){
      $_ =~ s/>.+/>$counter/;
      $counter++;
   }
   print;
}
