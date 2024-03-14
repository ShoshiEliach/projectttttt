#include <iostream>
#include <list>
#include <thread>
#include <chrono>
#include <mutex>
#include <condition_variable>
#include <stdio.h>
#include <ctime>
#include <vector>
#include <map>

//g++ -shared -o main.so -fPIC main.cpp


std::list<int> treadmillList;
std::mutex mtx_treadmill;

std::mutex waiterListMutex;

//std::list<int> myList;
std::list<int>::iterator lastMember;
std::condition_variable cv;

//std::mutex mtx_list;
int thisValue=0;

//מבנה של כמה רכבים מחכים עכשיו
struct Waiter {
    int number;
    std::time_t timeValue;

    Waiter(int num) : number(num) 
    {
    timeValue=std::time(nullptr);}
    //auto now = std::chrono::system_clock::now();
    //std::time_t timeValue = std::chrono::system_clock::to_time_t(now);    }
};
std::list<Waiter> waiterListA1={};
std::list<Waiter> waiterListA2={};
std::list<Waiter> waiterListB1={};
std::list<Waiter> waiterListB2={};
std::list<Waiter> waiterListC1={};
std::list<Waiter> waiterListC2={};
std::list<Waiter> waiterListD1={};
std::list<Waiter> waiterListD2={};

std::map<std::string, std::list<Waiter>> waiterListMap={};


// רשימת המזהים
std::vector<std::string> ids = {"A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2"};

// הוספת רשימות למילון



// void newValue(int value)
// {
// thisValue=value;
// }
// }
extern "C"{
std::list<Waiter>* findListById(const char* id) {
    std::string id_str(id);

 //mtx_treadmill.lock();

  /*for (int i = 0; i < ids.size(); i++) {
  std::string id = ids[i]; 

  // בדיקה אופציונלית: ודא שהמפתח (id) אינו קיים לפני הכנסת רשימה חדשה.
/*if (waiterListMap.find(id) == waiterListMap.end()) {
    waiterListMap[id] = list;
   }*/

 //mtx_treadmill.unlock();

  // איתור הרשימה במילון
  auto it = waiterListMap.find(id_str);

  // החזרת מצביע לרשימה אם נמצאה
  if (it != waiterListMap.end()) {
    return &it->second;
  }

  // החזרת nullptr אם הרשימה לא נמצאה
  return nullptr;
}
 void addValueToList(int value,std::list<Waiter> l)
{
   // std::unique_lock<std::mutex> lock(mtx_list);
    
   // waiterListMutex.lock();
    l.push_back(Waiter(value));
    //waiterListMutex.unlock();
}

int waiters(std::list<Waiter> l)
{
return l.size();
}




}

//פונקציה שעוברת על כל איבר ברשימה ובודקת אם עבר 4 שניות מאז שהוא נכנס מוציאה אותו
extern "C"{void countWaiters(std::list<Waiter> l)
{
  std::time_t current_time=std::time(nullptr);
          if(!l.empty())
            {
            for (size_t i = 0; i < l.size(); i++)
            {
          
              
                
                 //= treadmillList.front();
                //waiterListMutex.lock();
                std::time_t timeValueFirst = l.front().timeValue;
                //waiterListMutex.unlock();
                double timeDifference = std::difftime(current_time, timeValueFirst);
                if(timeDifference>=0.4)
                {
                    //waiterListMutex.lock();
                    l.pop_front();
                    //waiterListMutex.unlock();
                    //std::cout << waiterList.size() << std::endl;

                }
                /*else{
                std::cout << waiterList.size() << std::endl;
                break;
                }*/



                //int value=myList.front();
                //myList.pop_front();
                // Delete the value after 4 seconds
                //std::this_thread::sleep_for(std::chrono::seconds(4));
                //mtx_list.lock();
                //myList.remove(value);
                //mtx_list.unlock();
            }            }
}


}

extern "C" {
int main()
{

waiterListMap["A1"] = waiterListA1;
waiterListMap["A2"] = waiterListA2;
waiterListMap["B1"] = waiterListB1;
waiterListMap["B2"] = waiterListB2;
waiterListMap["C1"] = waiterListC1; 
waiterListMap["C2"] = waiterListC2;
waiterListMap["D1"] = waiterListD1;
waiterListMap["D2"] = waiterListD2;


 waiterListA1.push_back(Waiter(1));
 waiterListA2.push_back(Waiter(1));
 waiterListB1.push_back(Waiter(1));
 waiterListB2.push_back(Waiter(1));
 waiterListC1.push_back(Waiter(1));
 waiterListC2.push_back(Waiter(1));
 waiterListD1.push_back(Waiter(1));
 waiterListD2.push_back(Waiter(1));

 std::thread listA1 (countWaiters,waiterListA1);
 std::thread listA2 (countWaiters,waiterListA2);
 std::thread listB1 (countWaiters,waiterListB1);
 std::thread listB2 (countWaiters,waiterListB2);
 std::thread listC1 (countWaiters,waiterListC1);
 std::thread listC2 (countWaiters,waiterListC2);
 std::thread listD1 (countWaiters,waiterListD1);
 std::thread listD2 (countWaiters,waiterListD2);
listA1.join();
listA2.join();
listB1.join();
listB2.join();
listC1.join();
listC2.join();
listD1.join();
listD2.join();



    //std::thread add(addValueToList,thisValue);
    //std::thread treadmillThread(treadmill);
    //treadmillThread.join(); 
   // add.joinable();
    
    
    //printf("remove.join\n");


    return 0;
}

}

// extern "C" {
//     void addValueToList(int value) 
//     {
//         std::unique_lock<std::mutex> lock(mtx_list);
//         myList.push_back(value);
//         lastMember = std::prev(myList.end());
        
//     }

    
// }
// void deleteLastAfterDelay() {
//         std::this_thread::sleep_for(std::chrono::duration<double>(4.2));
//         {
//         std::unique_lock<std::mutex> lock(mtx_list);  
//         cv.wait(lock, []{ return !myList.empty(); });
        
//         myList.erase(lastMember);
            
            
//         }
//     }

// extern "C" {int waiters()
// {
//     int sum = 0;
//     std::unique_lock<std::mutex> lock(mtx_list); 
//     cv.wait(lock, []{ return !myList.empty(); });

//     for (int num : myList) 
//     {
//         sum += num;
//     }
    
//     return sum;

// }}

