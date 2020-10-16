import sys
import pygame
from bullet import Bullet
from alienship import Alien
from time import sleep
def start_game(sb, screen, setg, stats, aliens, ship, bullets):
	setg.initial_speed()
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	sb.prep_scrn()
	sb.prep_lives()
	sb.prep_level()
	stats.active_game = True
	aliens.empty()
	bullets.empty()
	new_fleet(screen, setg, aliens, ship)
	ship.reset_it()

def keydown_event(sb, event,screen, ship, setg, bullets, stats, aliens):
	if event.key == pygame.K_RIGHT:
				#move the ship to right
		ship.right = True
	elif event.key == pygame.K_LEFT:
		ship.left = True
	elif event.key == pygame.K_SPACE:
		fire_bull(screen, setg, ship, bullets)
	elif event.key == pygame.K_q:
		filename = 'highscore.txt'
		with open(filename, 'w') as file:
			file.write(str(stats.high_score))
		sys.exit()
	elif event.key == pygame.K_p:
		start_game(sb, screen, setg, stats, aliens, ship, bullets)
		

def keyup_event(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.right = False
	elif event.key == pygame.K_LEFT:
		ship.left = False

def click_check(sb, screen, setg, stats, play_button, m_x, m_y, aliens, ship, bullets):
	if play_button.rect.collidepoint(m_x, m_y) and  not stats.active_game:
		start_game(sb, screen, setg, stats, aliens, ship, bullets)
		

def chk_events(sb, screen, ship,setg, bullets, stats, play_button, aliens):
	#for keyboard and mouse movements
	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			filename = 'highscore.txt'
			with open(filename, 'w') as file:
				file.write(str(stats.high_score))
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_event(sb, event, screen, ship, setg, bullets, stats, aliens)

		elif event.type == pygame.KEYUP:
			keyup_event(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y  = pygame.mouse.get_pos()
			click_check(sb, screen, setg, stats, play_button, m_x, m_y, aliens, ship, bullets )


def fire_bull(screen, setg, ship, bullets):
	if len(bullets) < setg.bull_limit:
		new_bullet = Bullet(screen, setg, ship)
		bullets.add(new_bullet)

def check_high_score(sb, stats):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_highscrn()

def detect_collision(bullets, aliens, screen
	, setg, ship, stats, sb):
	dict_collision = pygame.sprite.groupcollide(
		bullets, aliens, True, True)
	#make third argument false to make super bullet
	if dict_collision:
		for aliens in dict_collision.values():
			stats.score += setg.hit_point*len(aliens)
		sb.prep_scrn()
	check_high_score(sb, stats)

	if len(aliens) ==0:
		stats.level += 1
		sb.prep_level()
		setg.progressive_speed()
		bullets.empty()#destroy old bullet
		new_fleet(screen, setg, aliens, ship)
				
def bullet_update(bullets, aliens, screen, 
	setg, ship, stats, sb):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	detect_collision(bullets, aliens, screen
		, setg, ship, stats, sb)
	

def get_aliennumber(setg, width):
	req_width = width #alien width
	avail_width = setg.scr_width - 2*req_width#margin
	number_of_alien = avail_width//(2*req_width)
	return number_of_alien

def create_alien(screen, setg, aliens, width
	, height, i,j):
	new_alien = Alien(screen, setg)
	posn_x = width  + 2*width*j#width = margin=alienwidth
	posn_y = height + 2*height*i + 10 #20 for scoreboard
	new_alien.rect.x = posn_x
	new_alien.rect.y = posn_y
	aliens.add(new_alien)

def get_rownumber(setg, height1, height2 ):
	avail_height = setg.scr_height - 4*height1 - height2
	number_of_rows  = avail_height//(2*height1)
	#number_of_rows = 3
	return number_of_rows  

def new_fleet(screen, setg, aliens, ship):
	new_alien = Alien(screen, setg)
	number_of_alien =  get_aliennumber(setg, new_alien.rect.width)
	number_of_rows = get_rownumber(setg, new_alien.rect.height, ship.rect.height)
	for i in range(number_of_rows):
		for j in range(number_of_alien):
			create_alien(screen, setg, aliens, new_alien.rect.width, new_alien.rect.height, i, j)

def change_direction(aliens, setg):
	for alien in aliens.sprites():
		alien.rect.y += setg.fleet_drop_factor
	setg.fleet_direcn *= -1

def check_edges(aliens, setg):
	for alien in aliens.sprites():
		if alien.check_edge_contact():
			change_direction(aliens, setg)
			break
def alien_attack(sb, stats, screen, setg, aliens, ship, bullets):
	if stats.ships_left >0:
		stats.ships_left -=1
		sb.prep_lives()
		sb.prep_level()
		aliens.empty()
		bullets.empty()
		new_fleet(screen, setg, aliens, ship)
		ship.reset_it()
		sleep(0.5)
	else:
		stats.active_game = False
		pygame.mouse.set_visible(True)
	


def check_floor_touch(sb, stats, screen, setg, aliens, ship, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			alien_attack(sb, stats, screen, setg, aliens, ship, bullets)
			break

def alien_update(sb, aliens, setg, ship, stats, screen , bullets):
	check_edges(aliens, setg)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		alien_attack(sb, stats, screen, setg, aliens, ship, bullets)
	check_floor_touch(sb, stats, screen, setg, aliens, ship, bullets)




def scr_update(setg, screen, ship, aliens, bullets
	, stats, play_button, sb, bg ):
#Redraw the screen during each pass through the loop.
    #Its old position will be colored over by the background.
    if stats.active_game:
    	#screen.fill(setg.bg_color)
    	bg.show1()
    	for bullet in bullets.sprites():
    		bullet.show()
    	ship.show()
    	aliens.draw(screen)
    	sb.show()

    if not stats.active_game:
    	#screen.fill((255,0,0))
    	bg.show()
    	play_button.show()
    #recently drawn screen
    pygame.display.flip()
