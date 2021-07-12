

import os
from  urllib  import  request
import time

os.system('clear')
print("""

 ****     **** *******      ********   ******       ** ******
/**/**   **/**/**////**    /**/////   **////**     /**//////*
/**//** ** /**/**   /**    /**       **    //      /**     /*
/** //***  /**/*******     /******* /**            /**     *
/**  //*   /**/**///**     /**////  /**            /**    *
/**   /    /**/**  //**  **/**      //**    ** **  /**   *
/**        /**/**   //**/**/******** //****** //*****   *
//         // //     // // ////////   //////   /////   /



#######################################
#                                     #
# Developer :Mr.ECJ7                  #
# Github    :@mrecj7                  #
# Tool      :telegram bX2             #
# version   :1.0                      #
#######################################




""")
id=input("Enter  telegarm id:")
mass=input("Enter massage:")
token="bot1800676900:AAGCsVFAKO1vQb0o0a1DSKyFU9bkmLzYpts"
api="https://api.telegram.org/"+token+"/sendMessage?chat_id="+id+"&text="+mass
print(api)
while 1==1:
 r=request.urlopen(api)
 print("atticking.")
 time.sleep(5)
else:
  print("some error found")
