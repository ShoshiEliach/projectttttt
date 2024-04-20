<<<<<<< HEAD
import heapq
=======
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
from sys import exit
import car
import pygame
import random
import lidar
<<<<<<< HEAD
import notIf
import points
import math
import networkx as nx
import trraficLight
import visualPoints
import datetime
=======
import points
import math

import trraficLight
import visualPoints
from datetime import datetime, timedelta
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
import threading
import time
import ctypes
import multiprocessing
import heapQ
<<<<<<< HEAD
from heapQ import lock
from multiprocessing import Process
import MacroGraph
=======
from multiprocessing import Process
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
#יבוא קובץ בC++ והגדרת הפונקציות
lib = ctypes.CDLL("C:\\Users\\User\\Documents\\projecttt\\Threads\\main.so")
newValue=lib.addValueToList
newValue.argtypes = [ctypes.c_int]

findListById=lib.findListById
lib.findListById.argtypes = [ctypes.c_char_p]
lib.findListById.restype = ctypes.POINTER(ctypes.c_void_p)
waiters_now=lib.waiters
waiters_now.restype = ctypes.c_int
waiters_now.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

<<<<<<< HEAD
addTimeToPriority=lib.updatePriority
addTimeToPriority.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
addTimeToPriority.restype = ctypes.c_int

WaitingLongTime=lib.WaitingLongTime
WaitingLongTime.restype = ctypes.c_char_p

initializeList=lib.initializeList
initializeList.argtypes = [ctypes.c_char_p]

#הגדרת תור העדיפויות של הנתיבים
=======
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
pqRoads = heapQ.PriorityQueue()
memberA1C1=heapQ.Member("A1C1",0,0,0,True)
memberA1A2=heapQ.Member("A1A2",0,0,0,True)
memberB1D1=heapQ.Member("B1D1",0,0,0,True)
memberB1B2=heapQ.Member("B1B2",0,0,0,True)
memberC1C2=heapQ.Member("C1C2",0,0,0,True)
memberD1D2=heapQ.Member("D1D2",0,0,0,True)
pqRoads.push(memberA1A2)
pqRoads.push(memberA1C1)
pqRoads.push(memberB1B2)
pqRoads.push(memberB1D1)
pqRoads.push(memberC1C2)
pqRoads.push(memberD1D2)
<<<<<<< HEAD

trrafics=[]
roadsGraph=MacroGraph.macroGraph
nodes_priority_queues=MacroGraph.node_priority_queues
def updateGraphFromHeapQMicro():
    temp_heap=pqRoads
    priority_queueB2=[]
    while temp_heap:
        temp_member=temp_heap.pop()
        heapq.heappush(priority_queueB2, (temp_member[1], temp_member[0]))

    heapq.heapify(priority_queueB2)
    nodes_priority_queues['nodeB2']=priority_queueB2

#פונקציה הבודקת על נתיב האם קרן הלידאר מתנגשת במכוניות שנמצאות בו אם כן מוסיפה את נקודת ההתנגשות לענן הנקודות
def identificationLidar(id,this_cars,lidar,all_points,isRed):
    timeWait = 0

    this_points = []#ההתנגשויות הנוכחיות
    if any(this_cars):#אם יש מכוניות בכלל
=======
trrafics=[]





#פונקציה הבודקת על נתיב האם קרן הלידאר מתנגשת במכוניות שנמצאות בו אם כן מוסיפה את נקודת ההתנגשות לענן הנקודות
def identificationLidar(id,this_cars,lidar,all_points,isRed):
    this_points = []#ההתנגשויות הנוכחיות
    if any(this_cars):#אם יש מכוניות בכלל
        #print(this_cars)
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
        cloud_points = []
        id_c_char_p = ctypes.c_char_p(id.encode())
        waiterList = findListById(id_c_char_p)

<<<<<<< HEAD
        # עובר על כל קרן ומחשב את נקודת הסיום שלה ומצייר אותה
=======

            #c_id = ctypes.c_void_p(waiterList)
            #print('c_id')
        # עובר על כל קרן ומחשב את נקודת הסיום שלה ומצייר אותה

>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
        for angle in range(lidar.start_angle, lidar.end_angle + 1):
            intersect_x, intersect_y = lidar.calculate_intersection_point(angle)
            this_points.append(((intersect_x, intersect_y), lidar.position))
        all_points.extend(this_points)

        # בודק על כל רכב בנתיב האם הוא נפגש בקרן
        for i in this_points:
            x, y = i[0]
<<<<<<< HEAD
            for c in this_cars:
                  if c.collided(x, y):
                    cloud_points.append((x, y))
            if (cloud_points):
                detection = points.carDetection(cloud_points, 4, 2)
                detection.detect_objects()
                # אם הרמזור ירוק צריך להסיר את המכוניות לאחר 4 שניות
                if not isRed:
                    lib.countWaiters(waiterList)
                else:
                    #מוסיף
                    timeWait=addTimeToPriority(waiterList)
                    '''print('timeWait')
                    print(timeWait)'''

                num = detection.get_detected_objects()
                '''print("num:")
                print(num)'''
                newValue(num, waiterList)
                mone = waiters_now(waiterList)
                ''''print("mone")
                print(mone)'''

                mone=mone+timeWait
                #print(id,mone)
                pqRoads.replace(id, mone)

                #כאן מעדכנים את הגרף מאקרו בערכי הצומת מיקרו
                updateGraphFromHeapQMicro()
                checkA1Orc1(id,mone)

                result = [id, mone]
                return result
=======
            #print(x, y)

            for c in this_cars:
                # try:
                #     print(c.vel)
                # except AttributeError:
                #     print("אובייקט זה אינו מכיל את התכונה 'vel'")
                if c.collided(x, y):
                    cloud_points.append((x, y))
                # עיבוד ענן הנקודות למספר הרכבים הממתינים
                if (cloud_points):
                    detection = points.carDetection(cloud_points, 4, 2)

                    detection.detect_objects()
                    if not isRed:
                        lib.countWaiters(waiterList)
                    num = detection.get_detected_objects()
                    #num = num // 2
                    #print(num)
                    newValue(num, waiterList)
                    mone = waiters_now(waiterList)
                    pqRoads.replace(id,mone)

                    print(id, mone)
                    result = [id, mone]
                    # print('result')
                    return result
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb


#פונקציה המזמנת את זיהוי הרכבים בשביל כל רשימת הנתיבים
def process_list(data):

    list_item,all_points = data
    id,list_data,lidar,isRed = list_item
<<<<<<< HEAD
=======
    #for l in list_data:
        #print( l.vel)

>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
    identificationLidar(id,list_data,lidar,all_points,isRed)




<<<<<<< HEAD
'''def callback(result):
    if isinstance(result, Exception):
        print(f"Error: {result}")
    else:
        print(f"Result: {result}")'''

#stop_thread = threading.Event()
def checkA1Orc1(id,mone):
  notIf.A1OrC1(id) and MacroGraph.add_cars_to_graph_Road(id,mone)



def on_specific_trrafic(id):
    #time.sleep(3)
    for t in trrafics:
        if t.id == id:
            t.on_trrafic()
            print('2')
            initializeList(id)
            green_wave(id)
        else:
            t.off_trrafic()
def on_trrafic_head_heapQ():
    if pqRoads.first_member:
        first_member = pqRoads.first_member
        #print("first_member")
        #print(first_member)

        id1 = first_member.id1
        id2 = first_member.id2
        print(id1,id2)
        on_specific_trrafic(id1)
        print('1')
        on_specific_trrafic(id2)



        first_member.counter = 0
        first_member.counter1 = 0
        first_member.counter2 = 0
        #task_thread.run = lambda: False
def diffrence_time(last,now,num_seconds):
    time_difference = last - now
    if time_difference.total_seconds() >= num_seconds:
        on_specific_trrafic(id)
        return True
    return False

def is_case_y():
    id=WaitingLongTime()
    if id !="not":
        return True,on_specific_trrafic,id
    else:
        return False,None,0





def traffic_light_logic():

    global is_green, elapsed_time
    elapsed_time=0
    is_green=False

    while True:
        if elapsed_time % 20 == 0:
            power_now = datetime.datetime.now()
            is_green = not is_green
            on_trrafic_head_heapQ()
        #פה צריך לבדוק את הזמן שרמזור דולק
        status, on_specific_trrafic, id = is_case_y()
        #print(status,is_green)

        if status and is_green and diffrence_time(power_now, (datetime.datetime.now()), 10):
            print('1.2')
            is_green = False
            print('1.5')
            on_specific_trrafic(id)

        time.sleep(1)
        elapsed_time += 1
'''def repeated_task():
    stop_thread = False
    while not stop_thread:
        time.sleep(20)
        check_on_trrafic()'''


#task_thread = threading.Thread(target=repeated_task)
=======
def callback(result):
    if isinstance(result, Exception):
        print(f"Error: {result}")
    else:
        print(f"Result: {result}")
stop_thread = threading.Event()
def check_on_trrafic():
    first_member = pqRoads.peek()
    id1 = first_member.id1
    id2 = first_member.id2
    first_member.counter = 0
    first_member.counter1 = 0
    first_member.counter2 = 0

    print(id1, id2)

    for t in trrafics:
        if t.id==id1 or t.id==id2:
            t.color=colors[1]
            t.fill(t.color)
            print(t.id)
            print('change color')
        else:
            t.color=colors[0]
            t.fill(t.color)
    task_thread.run = lambda: False


def repeated_task():
    stop_thread = False  # Flag to indicate thread termination
    while not stop_thread:
        # Call the function to do something
        check_on_trrafic()
        # Wait for 20 seconds before the next iteration
        time.sleep(20)

# Create a thread for the repeated task
task_thread = threading.Thread(target=repeated_task)
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb



lib.main()
<<<<<<< HEAD
#task_thread.start()
traffic_light_thread = threading.Thread(target=traffic_light_logic)
traffic_light_thread.start()
=======
task_thread.start()

>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb

if __name__ == '__main__':
    all_points = multiprocessing.Manager().list()

    # אתחול חלון הסימולציה
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    colors = [(255, 0, 0), (0, 255, 0)]
    pygame.display.set_caption('Smart junction')
    clock = pygame.time.Clock()

    roadAC = pygame.Surface((800, 200))
    roadAC.fill((255, 255, 0))


    trraficA1 = trraficLight.trraficWithPyg("A1",20,50,colors[0],300,220)
    trraficA1.fill(trraficA1.color)

    trraficA2 = trraficLight.trraficWithPyg("A2",20,50,colors[0],300,290)
    trraficA2.fill(trraficA2.color)

    trraficB1 = trraficLight.trraficWithPyg("B1",20,50,colors[0],330,550)
    trraficB1.fill(trraficB1.color)

    trraficB2=trraficLight.trraficWithPyg("B2", 20, 50, colors[0], 400,550)
    trraficB2.fill(trraficB2.color)

    trraficC1 = trraficLight.trraficWithPyg("C1",20,50,colors[0],530,280)
    trraficC1.fill(trraficC1.color)

    trraficC2 = trraficLight.trraficWithPyg("C2",20,50,colors[0],530,350)
    trraficC2.fill(trraficC2.color)

    trraficD1 = trraficLight.trraficWithPyg("D1",20,50,colors[0],400,120)
    trraficD1.fill(trraficD1.color)

    trraficD2 = trraficLight.trraficWithPyg("D2",20,50,colors[0],470,120)
    trraficD2.fill(trraficD2.color)

    trrafics=[trraficA1,trraficA2,trraficB1,trraficB2,trraficC1,trraficC2,trraficD1,trraficD2]

    roadBD = pygame.Surface((200, 600))
    roadBD.fill((0, 255, 255))

    lidar1Straight = lidar.Lidar((300, 290), -100, 360, 15, 0.35)
    lidar1Right = lidar.Lidar((300, 240), -100, 360, 15, 0.35)

    lidar2Straight = lidar.Lidar((400, 200), -200, -90, 10, 0.32)
    lidar2Right = lidar.Lidar((470, 200), -200, -90, 10, 0.32)

    lidar3Straight = lidar.Lidar((500, 310), -100, 180, 10, 0.35)
    lidar3Right = lidar.Lidar((500, 370), -100, 180, 10, 0.35)

    lidar4Straight = lidar.Lidar((330, 400), -200, 90, 10, 0.32)
    lidar4Right = lidar.Lidar((400, 400), -200, 90, 10, 0.32)

    max_cars = random.randrange(0, 15)
    carsA = []
    carsB = []
    carsC = []
    carsD = []


    pool = multiprocessing.Pool(processes=8)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # visualPoints.plotPoints2D(cloud_points)
                exit()

        screen.blit(roadAC, (0, 200))
        screen.blit(roadBD, (300, 0))
        screen.blit(trraficA1, (trraficA1.x,trraficA1.y))
        screen.blit(trraficA2, (trraficA2.x,trraficA2.y))
        screen.blit(trraficB1, (trraficB1.x,trraficB1.y))
        screen.blit(trraficB2, (trraficB2.x,trraficB2.y))
        screen.blit(trraficC1, (trraficC1.x,trraficC1.y))
        screen.blit(trraficC2, (trraficC2.x,trraficC2.y))
        screen.blit(trraficD1, (trraficD1.x,trraficD1.y))
        screen.blit(trraficD2, (trraficD2.x,trraficD2.y))
        # הוספת הרכבים לכביש באופן אקראי ורנדומלי
        if random.random() < 0.1:
            carsA.append(car.car(0.0, (random.randrange(200, 400))))
            carsB.append(car.car((random.randrange(300, 490)), 0.0))
            carsC.append(car.car(800.0, (random.randrange(200, 400))))
            carsD.append(car.car((random.randrange(300, 490)), 600.0))
        # הסעת הרכבים כל עוד הרמזור ירוק
        for c in carsA:
            if trraficA1.get_at((0, 0)) == (255, 0, 0) and c.x >= 250:
                c.vel = 0
            c.x += c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsB:
            if trraficB1.get_at((0, 0)) == (255, 0, 0) and c.y >= 250:
                c.vel = 0
            c.y += c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsC:
            if trraficC1.get_at((0, 0)) == (255, 0, 0) and c.x <= 500:
                c.vel = 0
            c.x -= c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))

        for c in carsD:
            if trraficD1.get_at((0, 0)) == (255, 0, 0) and c.y <= 400:
                c.vel = 0
            c.y -= c.vel
            pygame.draw.rect(screen, (255, 0, 0), (c.x, c.y, c.width, c.height))
        for i in range(len(all_points) - 1):
<<<<<<< HEAD
=======
            #print((points[i], points[i + 1]), (points[i + 2][0], points[i + 2][1]))
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
            x1, y1 = all_points[i][0]

            # Extract the x and y coordinates for the ending point
            x2, y2 = all_points[i][1]



            pygame.draw.line(screen, (128, 0, 128), (x1,y1),(x2,y2))

        lists_to_process = [("A1", carsA, lidar1Straight,trraficA1.trrafic_is_red()), ("A2", carsA, lidar1Right,trraficA2.trrafic_is_red()),
                            ("B1", carsB, lidar2Straight,trraficB1.trrafic_is_red()), ("B2", carsB, lidar2Right,trraficB2.trrafic_is_red()),
                            ("C1", carsC, lidar3Straight,trraficC1.trrafic_is_red()), ("C2", carsC, lidar3Right,trraficC2.trrafic_is_red()),
                            ("D1", carsD, lidar4Straight,trraficD1.trrafic_is_red()), ("D2", carsD, lidar4Right,trraficD2.trrafic_is_red())]

        #for list_item in lists_to_process:
            #pool.map_async(process_list, ((list_item,points),), callback=callback, chunksize=2)
        #pool.map_async(process_list, [(list_item, points) for list_item, points, _ in lists_to_process],
                           #callback=callback, chunksize=2)

<<<<<<< HEAD
        pool.map_async(process_list, [(list_item, all_points) for list_item in lists_to_process],
=======
        pool.map_async(process_list, [(list_item, all_points) for list_item in lists_to_process], callback=callback,
>>>>>>> 14ce2f7f1e0b518eb5bd25c8c2ba0de0ea596dcb
                       chunksize=2)

        pygame.display.update()
        clock.tick(60)
    pool.close()
    pool.join()







