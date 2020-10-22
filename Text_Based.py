import random

class Player:
	def __init__(self):
		self.hp = 10
		self.maxhp = 10
		self.dmg = 3
		self.ac = 0
	upg = 0
	gold = 0
	armor = "Clothing"
	hpupg = 0
	lockpicks = False

class Goblin:
	def __init__(self):
		self.hp = 9
		self.dmg = 2

class Spider:
	def __init__(self):
		self.hp = 6
		self.dmg = 3

class Orc:
	def __init__(self):
		self.hp = 18
		self.dmg = 4

player = Player()
battle = False
locked = False

print("You rest for a short while. You have been walking today for hours, but you've been traveling the known world for as long as you remember.\nNearby you see a small village, surrounded by the forest you are currently in.\nMaybe you will stay in this area a while, and see what is has to offer...")
while player.hp > 0:

	if player.hp > player.maxhp:
		player.hp = player.maxhp

	print("\nWould you like to continue onward? (Y/N)")
	ans = input().lower()

	if ans == "y":
		encounter = random.randint(1,100)
		if encounter < 10:
			locked = True
			while locked == True:
				print("You found a chest while out adventuring! It appears to be locked...Do you want to try and unlock it? (Y/N)")
				chest = input().lower()

				if chest != "y" and chest != "n":
					print("Please enter a valid action")

				elif chest == "y":
					unlock = random.randint(1,100)

					if player.lockpicks == True:
						if unlock <= 80:
							gold = random.randint(2,10)
							player.gold = player.gold + gold
							print(f"You opened the chest! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
							locked = False
						elif unlock > 80:
							print("Unfortunately, you were not able to open the chest")
							locked = False
							continue

					elif unlock > 80:
						gold = random.randint(2,10)
						player.gold = player.gold + gold
						print(f"You opened the chest! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
						locked = False

					elif unlock <= 80:
						print("Unfortunately, you were not able to open the chest")
						locked = False
						continue

				elif chest == "n":
					continue

		elif encounter >= 10:
			battle = True

			while battle == True:
				if player.upg == 0:
					enemy_class = random.choice([Goblin, Spider])
				else:
					enemy_class = random.choice([Goblin, Spider, Orc])

				enemy = enemy_class()
				enemy_name = enemy_class.__name__

				print(f"You encounter a {enemy_name}! (A to attack)")

				enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

				while enemy.hp > 0 or player.hp > 0:
					print("Press A to attack")
					user = input().lower()

					if user != "a" and user != "y":
						print("Please enter a valid action")
						continue

					if user == "a":
						enemy.hp = enemy.hp - player.dmg
						print(f"You dealt {player.dmg} damage to the {enemy_name}!")

					if enemy.hp <= 0:
						print("The enemy is slain!")
						battle = False

						loot = random.randint(1,100)

						if loot >= 70:
							print("Whats this...? You found a health potion on the corpse! Some of your wounds have been healed!")
							player.hp = player.hp + 5
							print(f"You now have {player.hp} health.")
						else:
							gold = random.randint(1, 4)
							player.gold = player.gold + gold

							print(f"Whats this..? You found {gold} gold on the corpse!\nYou now have {player.gold} gold!")
						break

					if user == "a":
						enemy.dmg = enemy.dmg + random.choice([0, 1]) - player.ac
						player.hp = player.hp - enemy.dmg

						if enemy.dmg > 0:
							print(f"The {enemy_name} hits back! it deals {enemy.dmg} damage to you!")
						elif enemy.dmg <= 0:
							print(f"The {enemy_name}'s blow was completely deflected by your {player.armor}!")
					if player.hp <= 0:

						print(f"The {enemy_name} knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
						player.gold = 0
						print(f"You now have {player.gold} gold")
						player.hp = 6
						battle = False
						break

	elif ans == "n":
		print(f"\n{player.hp} is your current health. {player.maxhp} is your maximum health currently.")
		print("You walk to the local village to stop at and rest for a while.\nThe local tavern costs 2 gold pieces to stay the night in,\nor you could go to the local marketplace and browse the various shops.\nYou can also see the steeple of a local church nearby, with it's high towers easily being the most noticeable object in the near vicinity.")
		print("\nWhere will you go? (Tavern/Market/Church)")
		village = input().lower()

		if village == "tavern":
			print(f"The tavern is bustling with the local folk. They offer drinks for one gold piece and rooms for two gold pieces. You have {player.gold} gold.\nOne of the innkeepers asks how they can help you. (Drink/Sleep)")

			inn = input().lower()

			if inn == "sleep":
				if player.gold < 2:
					print("\nYou do not have enough gold!")
					continue

				elif player.gold >= 2:
					cost = 2
					player.gold = player.gold - cost
					print(f"You stay the night at the Tavern and heal slightly.\nYou now have {player.gold} gold left in your pockets, and your health returns to {player.maxhp} health.")
					player.hp = player.maxhp

			if inn == "drink":
				if player.gold < 1:
					print("You do not have enough gold!")
					continue

				elif player.gold >= 1:
					cost = 1
					player.gold = player.gold - cost
					print(f"You stop at the bar and grab yourself a mug of grog to drink.\nYou now have {player.gold} gold left in your pockets.")
					drinking_event = random.randint(1,100)

					if drinking_event > 10 and drinking_event <= 30:
						print(f"The grog is especially good tonight. Warmth fills your veins and you feel renewed with energy and vigor.")
						player.hp = player.hp + 5
						print(f"{player.hp} is your current health. {player.maxhp} is your maximum health currently.")

					elif drinking_event >30 and drinking_event <=80:

						if player.gold >= 5:
							bad_bet = random.randint(1,5)
						elif player.gold >= 2 and player.gold < 5:
							bad_bet = random.randint(1,2)
						elif player. gold < 2:
							continue
						player.gold = player.gold - bad_bet
						print(f"Drinking was not such a good idea after all...while drunk, someone snatched {bad_bet} gold from your pockets...\nYou now have only {player.gold} gold left.")

					elif drinking_event >80:
						good_bet= random.randint(1,5)
						player.gold = player.gold + good_bet
						print(f"The night was filled with laughter and many bets! You won multiple bets, totaling in {good_bet} gold.\nYou now have {player.gold} gold!")



					elif drinking_event <= 10:

						print(f"While drunk, a tavern wench convinces you to join her in her room upstairs.\nWhile alone, she proceeds to demand all your gold and takes out a dagger.\nIt's no wench--it's a goblin in disguise!")
						enemy_class = Goblin()
						while enemy.hp > 0 or player.hp > 0:
							print("Press A to attack")
							user = input().lower()

							if user != "a" and user != "y":
								print("Please enter a valid action")
								continue

							if user == "a":
								enemy.hp = enemy.hp - player.dmg
								print(f"You dealt {player.dmg} damage to the goblin wench!")

							if enemy.hp <= 0:
								print("The enemy is slain!")

								loot = random.randint(1,100)
								if loot >= 70:
									print("Whats this...? You found a health potion on the corpse! Some of your wounds have been healed!")
									player.hp = player.hp + 5
								else:
									gold = random.randint(2, 5)
									player.gold = player.gold + gold

									print(f"Whats this..? You found {gold} gold on the corpse!")
								break

							if user == "a":
								player.hp = player.hp - enemy.dmg
								print(f"The goblin wench strikes back! it deals {enemy.dmg} damage to you!")

							if player.hp <= 0:

								print(f"The wench knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
								player.gold = 0
								print(f"You now have {player.gold} gold")
								player.hp = 5
								break


		elif village == "market" or village == "marketplace":
			print("The marketplace is booming with activity. The smell of milled grain and spices surrounds you. You can hear\nmetal-workers and craftsmen beating their hammers on their anvils.\nWhere will you go?(Armorer/Smith/Merchant)")
			market = input().lower()
			if market == "armory" or market == "armorer":
				print("The Armory is stocked with all sorts of armors and shields.\nThe smith procuring these wares asks if you'd care to examine any. (Y/N)")
				ans = input().lower()
				wares = ["Leather armor", "Steel armor"]
				leather_price = 8
				steel_price = 25
				if ans == "y":
					print(f"The smith says he currently has {wares} in stock. Would you care to purchase one?(Y/N)")
					ans2 = input().lower()

					if ans2 == "y":
						print(f"Which armor would you care to buy? The {wares[0]} costs {leather_price} and the {wares[1]} costs {steel_price}.\n{wares[0]} or {wares[1]}")
						ans3 = input().lower()

						if ans3 =="leather":
							if player.gold < leather_price:
								print("You do not have enough gold!")
							elif player.gold >= leather_price:
								player.gold = player.gold - leather_price
								print(f"The smith hands you the leather armor. Your armor level has increased!\nYou now have {player.gold} gold.")
								player.ac = 1
								player.armor = "Leather armor"

						if ans3 =="steel":
							if player.gold < steel_price:
								print("You do not have enough gold!")
								continue
							elif player.gold >= steel_price:
								player.gold = player.gold - steel_price
								print(f"The smith hands you the steel plate armor. Your armor level has increased!\nYou now have {player.gold} gold.")
								player.ac = 2
								player.upg = player.upg + 1
								player.armor = "Steel Plate armor"

					elif ans =="n":	
						print("The smith nods and asks you to come back if you change your mind.")
						continue
				elif ans == "n":
					print("The smith nods and asks you to come back if you change your mind.")
					continue


			if market == "smith" or market == "blacksmith":

				if player.upg == 0:
					cost = 10

					print(f"The blacksmith agrees to upgrade your sword for {cost} gold. You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)")
					upgrade = input().lower()
					if upgrade == "y":
						if player.gold < cost:
							print("You do not have enough gold!")
							continue
						elif player.gold >= cost:
							player.gold = player.gold - cost
							print("The blacksmith upgraded your sword. You now do more damage per hit!")
							player.dmg = player.dmg + 2
							player.upg = player.upg + 1
						elif upgrade == "n":
							continue

				elif player.upg == 1:
					cost = 25

					print(f"The blacksmith agrees to upgrade your sword for {cost} gold. You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)")
					upgrade = input().lower()
					if upgrade == "y":
						if player.gold < cost:
							print("You do not have enough gold!")
							continue
						elif player.gold >= cost:
							player.gold = player.gold - cost
							print("The blacksmith upgraded your sword. You now do more damage per hit!")
							player.dmg = player.dmg + 2
							player.upg = player.upg + 1
					elif upgrade == "n":
						continue
		

				elif player.upg == 2:
					cost = 50

					print(f"The blacksmith agrees to upgrade your sword for {cost} gold. You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)")
					upgrade = input().lower()
					if upgrade == "y":
						if player.gold < cost:
							print("You do not have enough gold!")
							continue
						elif player.gold >= cost:
							player.gold = player.gold - cost
							print("The blacksmith upgraded your sword. You now do more damage per hit!")
							player.dmg = player.dmg + 2
							player.upg = player.upg + 1

					elif upgrade == "n":
						continue

				elif player.upg >= 3:
					print(f"The blacksmith tells you that he cannot upgrade your blade any further. If you want a better blade, he recommends searching for someone more skilled.")
					continue


			elif market == "merchant":
				print("The beady-eyed merchant eyes your coin purse greedily. He immediately asks if you'd care to browse his wares. (Y/N)")
				merchant = input().lower()

				if merchant == "y":
					price = 20
					wares = ["lockpicks",]
					print(f"The merchant tells you he currently has {wares} in stock. They cost {price} gold. Would you like to buy them? (Y/N)")
					ans = input().lower()
					if ans =="y":
						if player.gold < price:
							print("You do not have enough gold!")
							continue

						elif player.gold >= price:
							player.gold = player.gold - price
							player.lockpicks = True
							print(f"You bought the {wares}! You now have {player.gold} gold left")
					elif ans =="n":
						print("The merchant yells at you angrily for wasting his time, and demands you leave him be.")
						continue

				elif merchant =="n":
					print("The merchant yells at you angrily for wasting his time, and demands you leave him be.")
					continue
			else:
				print("Please enter a valid action")
				continue

		elif village == "church":

			if player.hpupg == 2:
						print("The church is abandoned. The floor is covered in dust, the windows borded up, and there is no evidence of anyone having been there in years.")
						continue
			else:			
				print('You enter the modest village church, with a few small wooden benches and stools scattered around.\nYou see an elderly man in dark monk robes kneeling before an altar to a god unbeknownst to you.\nWithout turning around, he asks what you seek here.\n"Health?" He asks. (Y/N)')
				ans = input().lower()

				if player.hpupg == 0:
					price = 15
				elif player.hpupg == 1:
					price = 50

				if ans == "y":
					print(f'"I can aid you in that, with powers deemed unnatural by some."\n"But this does not come without a price. {price} gold will do for now."\n"Do you agree to this?"(Y/N)')
					ans2 = input().lower()

					if ans2 == "y":
							if player.gold < price:
								print('"My my my... not enough gold..."')
								continue
							elif player.gold >= price:
								player.gold = player.gold - price
								player.maxhp = player.maxhp + 5
								print('"Mmhm...There you are. Go now; and reap the benefits of your increased fortitude"')
								player.hpupg = player.hpupg + 1
								continue

			
					elif ans2 == "n":
						print('"Then please, leave me to my work."')
						continue

				if ans == "n":
					print('"Then please, leave me to my work."')
					continue


		else:
			print("Please enter a valid action")
			continue


	else:
		print("Please enter a valid action")
		continue
	