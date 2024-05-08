import pygame
import time
import random
import sqlite3

connection = sqlite3.connect('Max_result_database.db')
cursor = connection.cursor()

pygame.init()
lvl = 1

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 30, 30)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (201,100,59)

dis_width = 1000
dis_height = 800
pos = 'up'

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake_block = 10
snake_speed_0 = 15

# Загрузка текстуры
texture_up = pygame.image.load('face_test_up.png')
texture_down = pygame.image.load('face_test_down.png')
texture_right = pygame.image.load('face_test_right.png')
texture_left = pygame.image.load('face_test_left.png')

linux_logo = pygame.image.load('Linux_Logo.png')

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def record_max_result(Length_of_snake):
    import sqlite3
    # Имя файла базы данных
    db_name = 'max_result.db'
    # Создаем соединение с базой данных или создаем новую базу данных, если она не существует
    conn = sqlite3.connect(db_name)
    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()
    # Создаем таблицу с одним столбцом 'results' типа INTEGER, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS max_result
                      (results INTEGER)''')
    # Переменная со значением для записи в столбец 'results'
    value_to_insert = int(Length_of_snake-1)
    # Подготавливаем SQL-запрос для вставки данных
    sql = "INSERT INTO max_result (results) VALUES (?)"
    # Выполняем SQL-запрос для вставки данных
    cursor.execute(sql, (value_to_insert,))
    # Сохраняем изменения в базе данных
    conn.commit()
    # Находим максимальное значение в столбце 'results'
    cursor.execute("SELECT MAX(results) FROM max_result")
    max_res = cursor.fetchone()[0]
    # Закрываем соединение с базой данных
    conn.close()
    return max_res


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [10, 0])

def Your_level(level):
    value = score_font.render("level: " + str(level), True, yellow)
    dis.blit(value, [800, 3])


def our_snake(snake_block, snake_list, position):
    b = 0
    for x in snake_list:
        rect = pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        if b == (len(snake_list)-1):
            if position == 'up':
                for z in range(rect.left, rect.right, texture_up.get_width()):
                    for y in range(rect.top, rect.bottom, texture_up.get_height()):
                        dis.blit(texture_up, (z, y))
            elif position == 'down':
                for z in range(rect.left, rect.right, texture_down.get_width()):
                    for y in range(rect.top, rect.bottom, texture_down.get_height()):
                        dis.blit(texture_down, (z, y))
            elif position == 'right':
                for z in range(rect.left, rect.right, texture_right.get_width()):
                    for y in range(rect.top, rect.bottom, texture_right.get_height()):
                        dis.blit(texture_right, (z, y))
            elif position == 'left':
                for z in range(rect.left, rect.right, texture_left.get_width()):
                    for y in range(rect.top, rect.bottom, texture_left.get_height()):
                        dis.blit(texture_left, (z, y))
        b += 1


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def main():
    

def gameLoop(before_r_l, before_up_down, snake_speed, This_time, check_update, pos):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block - 40) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block - 40) / 10.0) * 10.0


    while not game_over:
        while game_close == True:
            if check_update == True:
                record = record_max_result(Length_of_snake)
                check_update = False

                value = score_font.render("Your Record: " + str(record), True, yellow)
                dis.blit(value, [300, 0])
                pygame.display.update()

            message("Game over! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(0, 0, 10, time.time(), True, 'up')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and before_r_l != 1 and time.time() - This_time >= 0.005:
                    pos = 'left'
                    before_up_down = 0
                    x1_change = -snake_block
                    y1_change = 0
                    before_r_l = 1
                    This_time = time.time()
                elif event.key == pygame.K_RIGHT and before_r_l != 1 and time.time() - This_time >= 0.005:
                    pos = 'right'
                    before_up_down = 0
                    x1_change = snake_block
                    y1_change = 0
                    before_r_l = 1
                    This_time = time.time()
                elif event.key == pygame.K_UP and before_up_down == 0 and time.time() - This_time >= 0.005:
                    pos = 'up'
                    before_up_down = 1
                    y1_change = -snake_block
                    x1_change = 0
                    before_r_l = 0
                    This_time = time.time()
                elif event.key == pygame.K_DOWN and before_up_down == 0 and time.time() - This_time >= 0.005:
                    pos = 'down'
                    before_up_down = 1
                    y1_change = snake_block
                    x1_change = 0
                    before_r_l = 0
                    This_time = time.time()

        if x1 >= dis_width+1:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width
        elif y1 < 0:
            y1 = dis_height
        elif y1 >= dis_height+1:
            y1 = 0

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        #прямоугольники (препятствия и графика)
        coord_rect = [0, 50, 250, 15]
        pygame.draw.rect(dis, brown, [coord_rect[0], coord_rect[1], coord_rect[2], coord_rect[3]])

        coord_rect_1 = [250, 0, 15, 65]
        pygame.draw.rect(dis, brown, [coord_rect_1[0], coord_rect_1[1], coord_rect_1[2], coord_rect_1[3]])

        coord_rect_2 = [450, 300, 250, 250]
        rect_1 = pygame.draw.rect(dis, blue, [coord_rect_2[0], coord_rect_2[1], coord_rect_2[2], coord_rect_2[3]])
        for z in range(rect_1.left, rect_1.right, linux_logo.get_width()):
            for y in range(rect_1.top, rect_1.bottom, linux_logo.get_height()):
                dis.blit(linux_logo, (z, y))

        coord_rect_3 = [790, 280, 15, 320]
        pygame.draw.rect(dis, brown, [coord_rect_3[0], coord_rect_3[1], coord_rect_3[2], coord_rect_3[3]])

        coord_rect_4 = [700, 600, 105, 15]
        pygame.draw.rect(dis, brown, [coord_rect_4[0], coord_rect_4[1], coord_rect_4[2], coord_rect_4[3]])

        coord_rect_5 = [700, 600, 15, 300]
        pygame.draw.rect(dis, brown, [coord_rect_5[0], coord_rect_5[1], coord_rect_5[2], coord_rect_5[3]])

        coord_rect_6 = [790, 270, 300, 15]
        pygame.draw.rect(dis, brown, [coord_rect_6[0], coord_rect_6[1], coord_rect_6[2], coord_rect_6[3]])

        coord_rect_7 = [0, 0, 250, 10]
        pygame.draw.rect(dis, brown, [coord_rect_7[0], coord_rect_7[1], coord_rect_7[2], coord_rect_7[3]])

        coord_rect_8 = [785, 0, 300, 10]
        pygame.draw.rect(dis, brown, [coord_rect_8[0], coord_rect_8[1], coord_rect_8[2], coord_rect_8[3]])

        coord_rect_9 = [785, 0, 10, 50]
        pygame.draw.rect(dis, brown, [coord_rect_9[0], coord_rect_9[1], coord_rect_9[2], coord_rect_9[3]])

        coord_rect_10 = [785, 50, 250, 10]
        pygame.draw.rect(dis, brown, [coord_rect_10[0], coord_rect_10[1], coord_rect_10[2], coord_rect_10[3]])

        coord_rect_11 = [785, 50, 250, 10]
        pygame.draw.rect(dis, brown, [coord_rect_11[0], coord_rect_11[1], coord_rect_11[2], coord_rect_11[3]])

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        list_cord_game_over_x = []
        list_cord_game_over_y = []
        for i in range (int(coord_rect[0]), int(coord_rect[0]) + int(coord_rect[2])):
            list_cord_game_over_x.append(i)

        for o in range (int(coord_rect[1]), int(coord_rect[1]) + int(coord_rect[3])):
            list_cord_game_over_y.append(o)

        #второе препятствие:
        for i in range (int(coord_rect_1[0]), int(coord_rect_1[0]) + int(coord_rect_1[2])):
            list_cord_game_over_x.append(i)

        for o in range (int(coord_rect_1[1]), int(coord_rect_1[1]) + int(coord_rect_1[3])):
            list_cord_game_over_y.append(o)

        #3
        obstacles_3_x = []
        obstacles_3_y = []
        for i in range (int(coord_rect_3[0]), int(coord_rect_3[0]) + int(coord_rect_3[2])):
            obstacles_3_x.append(i)

        for o in range (int(coord_rect_3[1]), int(coord_rect_3[1]) + int(coord_rect_3[3])):
            obstacles_3_y.append(o)

        #4
        obstacles_4_x = []
        obstacles_4_y = []
        for i in range (int(coord_rect_4[0]), int(coord_rect_4[0]) + int(coord_rect_4[2])):
            obstacles_4_x.append(i)

        for o in range (int(coord_rect_4[1]), int(coord_rect_4[1]) + int(coord_rect_4[3])):
            obstacles_4_y.append(o)

        obstacles_5_x = []
        obstacles_5_y = []
        for i in range(int(coord_rect_5[0]), int(coord_rect_5[0]) + int(coord_rect_5[2])):
            obstacles_5_x.append(i)

        for o in range(int(coord_rect_5[1]), int(coord_rect_5[1]) + int(coord_rect_5[3])):
            obstacles_5_y.append(o)

        obstacles_6_x = []
        obstacles_6_y = []
        for i in range(int(coord_rect_6[0]), int(coord_rect_6[0]) + int(coord_rect_6[2])):
            obstacles_6_x.append(i)

        for o in range(int(coord_rect_6[1]), int(coord_rect_6[1]) + int(coord_rect_6[3])):
            obstacles_6_y.append(o)


        if (x1 in list_cord_game_over_x and y1 in list_cord_game_over_y) or (
                x1 in obstacles_3_x and y1 in obstacles_3_y) or (
                x1 in obstacles_4_x and y1 in obstacles_4_y) or (
                x1 in obstacles_5_x and y1 in obstacles_5_y) or (
                x1 in obstacles_6_x and y1 in obstacles_6_y) or (
                x1 < 250 and y1 < 70) or (x1 > 775 and y1 < 60):
            game_close = True
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        our_snake(snake_block, snake_List, pos)

        Your_score(Length_of_snake - 1)
        Your_level(lvl)


        list_foodx = []
        for i in range(100):
            list_foodx.append(i)

        list_foody = []
        for i in range(51):
            list_foody.append(i)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 0.5

        while (foodx in list_foodx and foody in list_foody) or (
                foodx in list_cord_game_over_x and foody in list_cord_game_over_y) or (
                foodx in obstacles_3_x and foody in obstacles_3_y) or (
                foodx in obstacles_4_x and foody in obstacles_4_y) or (
                foodx in obstacles_5_x and foody in obstacles_5_y) or (
                foodx in obstacles_6_x and foody in obstacles_6_y) or (
                foodx < 250 and foody < 65) or (foodx > 775 and foody < 60):
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        pygame.display.update()

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop(0, 0, snake_speed_0, 0, True, 'up')