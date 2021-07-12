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
  # Github    :@MrECJ7                 #
  # Tool      :telegram bX2             #
  # version   :1.0                      #
  #######################################




""")
id=input("Enter  telegarm id:")
mass=input("Enter massage:")
#Replace the API with your own bot token 
token="1795709734:AAHy2j_kf477RZt8Zb_1lQYfnnUYnPSMWn4"
api="https://api.telegram.org/"+token+"/sendMessage?chat_id="+id+"&text="+mass
print(api)
while 1==1:
 r=request.urlopen(api)
 print("atticking.")
 time.sleep(5)
else:
  print("some error found")
