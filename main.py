from sys import exit
import car
import pygame
import random
import lidar
import points
import math

import trraficLight
import visualPoints
from datetime import datetime, timedelta
import threading
import time
import ctypes
import multiprocessing
import heapQ
from multiprocessing import Process
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
trrafics=[]





#פונקציה הבודקת על נתיב האם קרן הלידאר מתנגשת במכוניות שנמצאות בו אם כן מוסיפה את נקודת ההתנגשות לענן הנקודות
def identificationLidar(id,this_cars,lidar,all_points,isRed):
    this_points = []#ההתנגשויות הנוכחיות
    if any(this_cars):#אם יש מכוניות בכלל
        #print(this_cars)
        cloud_points = []
        id_c_char_p = ctypes.c_char_p(id.encode())
        waiterList = findListById(id_c_char_p)


            #c_id = ctypes.c_void_p(waiterList)
            #print('c_id')
        # עובר על כל קרן ומחשב את נקודת הסיום שלה ומצייר אותה

        for angle in range(lidar.start_angle, lidar.end_angle + 1):
            intersect_x, intersect_y = lidar.calculate_intersection_point(angle)
            this_points.append(((intersect_x, intersect_y), lidar.position))
        all_points.extend(this_points)

        # בודק על כל רכב בנתיב האם הוא נפגש בקרן
        for i in this_points:
            x, y = i[0]
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


#פונקציה המזמנת את זיהוי הרכבים בשביל כל רשימת הנתיבים
def process_list(data):

    list_item,all_points = data
    id,list_data,lidar,isRed = list_item
    #for l in list_data:
        #print( l.vel)

    identificationLidar(id,list_data,lidar,all_points,isRed)




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



lib.main()
task_thread.start()


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
            #print((points[i], points[i + 1]), (points[i + 2][0], points[i + 2][1]))
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

        pool.map_async(process_list, [(list_item, all_points) for list_item in lists_to_process], callback=callback,
                       chunksize=2)

        pygame.display.update()
        clock.tick(60)
    pool.close()
    pool.join()







