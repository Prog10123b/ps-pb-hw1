from time import sleep
from os import system


page1 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
             $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
  $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
              $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

page2 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                   $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
           $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

if __name__ != "__main__":
    exit()

for i in range(4):
    sleep(1)
    system("cls")
    print(page1, end="\r")

    sleep(1)
    system("cls")
    print(page2, end="\r")