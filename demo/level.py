import numpy as np

scene_dict = {'airfield': 0, 'airplane_cabin': 1, 'airport_terminal': 2, 'alcove': 3, 'alley': 4, 'amphitheater': 5, 'amusement_arcade': 6, 'amusement_park': 7, 'apartment_building/outdoor': 8, 'aquarium': 9, 'aqueduct': 10, 'arcade': 11, 'arch': 12, 'archaelogical_excavation': 13, 'archive': 14, 'arena/hockey': 15, 'arena/performance': 16, 'arena/rodeo': 17, 'army_base': 18, 'art_gallery': 19, 'art_school': 20, 'art_studio': 21, 'artists_loft': 22, 'assembly_line': 23, 'athletic_field/outdoor': 24, 'atrium/public': 25, 'attic': 26, 'auditorium': 27, 'auto_factory': 28, 'auto_showroom': 29, 'badlands': 30, 'bakery/shop': 31, 'balcony/exterior': 32, 'balcony/interior': 33, 'ball_pit': 34, 'ballroom': 35, 'bamboo_forest': 36, 'bank_vault': 37, 'banquet_hall': 38, 'bar': 39, 'barn': 40, 'barndoor': 41, 'baseball_field': 42, 'basement': 43, 'basketball_court/indoor': 44, 'bathroom': 45, 'bazaar/indoor': 46, 'bazaar/outdoor': 47, 'beach': 48, 'beach_house': 49, 'beauty_salon': 50, 'bedchamber': 51, 'bedroom': 52, 'beer_garden': 53, 'beer_hall': 54, 'berth': 55, 'biology_laboratory': 56, 'boardwalk': 57, 'boat_deck': 58, 'boathouse': 59, 'bookstore': 60, 'booth/indoor': 61, 'botanical_garden': 62, 'bow_window/indoor': 63, 'bowling_alley': 64, 'boxing_ring': 65, 'bridge': 66, 'building_facade': 67, 'bullring': 68, 'burial_chamber': 69, 'bus_interior': 70, 'bus_station/indoor': 71, 'butchers_shop': 72, 'butte': 73, 'cabin/outdoor': 74, 'cafeteria': 75, 'campsite': 76, 'campus': 77, 'canal/natural': 78, 'canal/urban': 79, 'candy_store': 80, 'canyon': 81, 'car_interior': 82, 'carrousel': 83, 'castle': 84, 'catacomb': 85, 'cemetery': 86, 'chalet': 87, 'chemistry_lab': 88, 'childs_room': 89, 'church/indoor': 90, 'church/outdoor': 91, 'classroom': 92, 'clean_room': 93, 'cliff': 94, 'closet': 95, 'clothing_store': 96, 'coast': 97, 'cockpit': 98, 'coffee_shop': 99, 'computer_room': 100, 'conference_center': 101, 'conference_room': 102, 'construction_site': 103, 'corn_field': 104, 'corral': 105, 'corridor': 106, 'cottage': 107, 'courthouse': 108, 'courtyard': 109, 'creek': 110, 'crevasse': 111, 'crosswalk': 112, 'dam': 113, 'delicatessen': 114, 'department_store': 115, 'desert/sand': 116, 'desert/vegetation': 117, 'desert_road': 118, 'diner/outdoor': 119, 'dining_hall': 120, 'dining_room': 121, 'discotheque': 122, 'doorway/outdoor': 123, 'dorm_room': 124, 'downtown': 125, 'dressing_room': 126, 'driveway': 127, 'drugstore': 128, 'elevator/door': 129, 'elevator_lobby': 130, 'elevator_shaft': 131, 'embassy': 132, 'engine_room': 133, 'entrance_hall': 134, 'escalator/indoor': 135, 'excavation': 136, 'fabric_store': 137, 'farm': 138, 'fastfood_restaurant': 139, 'field/cultivated': 140, 'field/wild': 141, 'field_road': 142, 'fire_escape': 143, 'fire_station': 144, 'fishpond': 145, 'flea_market/indoor': 146, 'florist_shop/indoor': 147, 'food_court': 148, 'football_field': 149, 'forest/broadleaf': 150, 'forest_path': 151, 'forest_road': 152, 'formal_garden': 153, 'fountain': 154, 'galley': 155, 'garage/indoor': 156, 'garage/outdoor': 157, 'gas_station': 158, 'gazebo/exterior': 159, 'general_store/indoor': 160, 'general_store/outdoor': 161, 'gift_shop': 162, 'glacier': 163, 'golf_course': 164, 'greenhouse/indoor': 165, 'greenhouse/outdoor': 166, 'grotto': 167, 'gymnasium/indoor': 168, 'hangar/indoor': 169, 'hangar/outdoor': 170, 'harbor': 171, 'hardware_store': 172, 'hayfield': 173, 'heliport': 174, 'highway': 175, 'home_office': 176, 'home_theater': 177, 'hospital': 178, 'hospital_room': 179, 'hot_spring': 180, 'hotel/outdoor': 181, 'hotel_room': 182, 'house': 183, 'hunting_lodge/outdoor': 184, 'ice_cream_parlor': 185, 'ice_floe': 186, 'ice_shelf': 187, 'ice_skating_rink/indoor': 188, 'ice_skating_rink/outdoor': 189, 'iceberg': 190, 'igloo': 191, 'industrial_area': 192, 'inn/outdoor': 193, 'islet': 194, 'jacuzzi/indoor': 195, 'jail_cell': 196, 'japanese_garden': 197, 'jewelry_shop': 198, 'junkyard': 199, 'kasbah': 200, 'kennel/outdoor': 201, 'kindergarden_classroom': 202, 'kitchen': 203, 'lagoon': 204, 'lake/natural': 205, 'landfill': 206, 'landing_deck': 207, 'laundromat': 208, 'lawn': 209, 'lecture_room': 210, 'legislative_chamber': 211, 'library/indoor': 212, 'library/outdoor': 213, 'lighthouse': 214, 'living_room': 215, 'loading_dock': 216, 'lobby': 217, 'lock_chamber': 218, 'locker_room': 219, 'mansion': 220, 'manufactured_home': 221, 'market/indoor': 222, 'market/outdoor': 223, 'marsh': 224, 'martial_arts_gym': 225, 'mausoleum': 226, 'medina': 227, 'mezzanine': 228, 'moat/water': 229, 'mosque/outdoor': 230, 'motel': 231, 'mountain': 232, 'mountain_path': 233, 'mountain_snowy': 234, 'movie_theater/indoor': 235, 'museum/indoor': 236, 'museum/outdoor': 237, 'music_studio': 238, 'natural_history_museum': 239, 'nursery': 240, 'nursing_home': 241, 'oast_house': 242, 'ocean': 243, 'office': 244, 'office_building': 245, 'office_cubicles': 246, 'oilrig': 247, 'operating_room': 248, 'orchard': 249, 'orchestra_pit': 250, 'pagoda': 251, 'palace': 252, 'pantry': 253, 'park': 254, 'parking_garage/indoor': 255, 'parking_garage/outdoor': 256, 'parking_lot': 257, 'pasture': 258, 'patio': 259, 'pavilion': 260, 'pet_shop': 261, 'pharmacy': 262, 'phone_booth': 263, 'physics_laboratory': 264, 'picnic_area': 265, 'pier': 266, 'pizzeria': 267, 'playground': 268, 'playroom': 269, 'plaza': 270, 'pond': 271, 'porch': 272, 'promenade': 273, 'pub/indoor': 274, 'racecourse': 275, 'raceway': 276, 'raft': 277, 'railroad_track': 278, 'rainforest': 279, 'reception': 280, 'recreation_room': 281, 'repair_shop': 282, 'residential_neighborhood': 283, 'restaurant': 284, 'restaurant_kitchen': 285, 'restaurant_patio': 286, 'rice_paddy': 287, 'river': 288, 'rock_arch': 289, 'roof_garden': 290, 'rope_bridge': 291, 'ruin': 292, 'runway': 293, 'sandbox': 294, 'sauna': 295, 'schoolhouse': 296, 'science_museum': 297, 'server_room': 298, 'shed': 299, 'shoe_shop': 300, 'shopfront': 301, 'shopping_mall/indoor': 302, 'shower': 303, 'ski_resort': 304, 'ski_slope': 305, 'sky': 306, 'skyscraper': 307, 'slum': 308, 'snowfield': 309, 'soccer_field': 310, 'stable': 311, 'stadium/baseball': 312, 'stadium/football': 313, 'stadium/soccer': 314, 'stage/indoor': 315, 'stage/outdoor': 316, 'staircase': 317, 'storage_room': 318, 'street': 319, 'subway_station/platform': 320, 'supermarket': 321, 'sushi_bar': 322, 'swamp': 323, 'swimming_hole': 324, 'swimming_pool/indoor': 325, 'swimming_pool/outdoor': 326, 'synagogue/outdoor': 327, 'television_room': 328, 'television_studio': 329, 'temple/asia': 330, 'throne_room': 331, 'ticket_booth': 332, 'topiary_garden': 333, 'tower': 334, 'toyshop': 335, 'train_interior': 336, 'train_station/platform': 337, 'tree_farm': 338, 'tree_house': 339, 'trench': 340, 'tundra': 341, 'underwater/ocean_deep': 342, 'utility_room': 343, 'valley': 344, 'vegetable_garden': 345, 'veterinarians_office': 346, 'viaduct': 347, 'village': 348, 'vineyard': 349, 'volcano': 350, 'volleyball_court/outdoor': 351, 'waiting_room': 352, 'water_park': 353, 'water_tower': 354, 'waterfall': 355, 'watering_hole': 356, 'wave': 357, 'wet_bar': 358, 'wheat_field': 359, 'wind_farm': 360, 'windmill': 361, 'yard': 362, 'youth_hostel': 363, 'zen_garden': 364, }
object_dict = {'face': 0, 'person': 1, 'bicycle': 2, 'car': 3, 'motorbike': 4, 'aeroplane': 5, 'bus': 6, 'train': 7, 'truck': 8, 'boat': 9, 'traffic light': 10, 'fire hydrant': 11, 'stop sign': 12, 'parking meter': 13, 'bench': 14, 'bird': 15, 'cat': 16, 'dog': 17, 'horse': 18, 'sheep': 19, 'cow': 20, 'elephant': 21, 'bear': 22, 'zebra': 23, 'giraffe': 24, 'backpack': 25, 'umbrella': 26, 'handbag': 27, 'tie': 28, 'suitcase': 29, 'frisbee': 30, 'skis': 31, 'snowboard': 32, 'sports ball': 33, 'kite': 34, 'baseball bat': 35, 'baseball glove': 36, 'skateboard': 37, 'surfboard': 38, 'tennis racket': 39, 'bottle': 40, 'wine glass': 41, 'cup': 42, 'fork': 43, 'knife': 44, 'spoon': 45, 'bowl': 46, 'banana': 47, 'apple': 48, 'sandwich': 49, 'orange': 50, 'broccoli': 51, 'carrot': 52, 'hot dog': 53, 'pizza': 54, 'donut': 55, 'cake': 56, 'chair': 57, 'sofa': 58, 'pottedplant': 59, 'bed': 60, 'diningtable': 61, 'toilet': 62, 'tvmonitor': 63, 'laptop': 64, 'mouse': 65, 'remote': 66, 'keyboard': 67, 'cell phone': 68, 'microwave': 69, 'oven': 70, 'toaster': 71, 'sink': 72, 'refrigerator': 73, 'book': 74, 'clock': 75, 'vase': 76, 'scissors': 77, 'teddy bear': 78, 'hair drier': 79, 'toothbrush': 80, }

class privacyLevel():
	def __init__(self, object_dict=object_dict, scene_dict=scene_dict, n=3, learning_rate=0.5):
		#初始化
		#n为最高隐私级别，隐私级别从0开始
		#object_dict为字典，格式为{object_class:object_id}, object_id从0开始
		#scene_dict为字典，格式为{scene_class:scene_id}, scene_id从0开始
		#learning_rate为学习率，控制参数更新的幅度
		self.object_dict = object_dict
		self.scene_dict = scene_dict #scene_dict[scene_class]=scene_id
		self.learning_rate = learning_rate #学习率
		self.max_level = n #设置最大隐私级别

		#问询图片总数
		self.imgNum=0
		# singleAppear[s][i]表示scene s中object i在问询时出现的次数
		self.singleAppear=np.zeros((len(self.scene_dict),len(self.object_dict)),dtype='uint16')
		# coAppear[s][i][j]表示scene s中object i与object j同时出现的次数
		self.coAppear = np.zeros((len(self.scene_dict),len(self.object_dict),len(self.object_dict)), dtype='uint16')
		# coLevel[s][i][j]表示scene s中object i与object j同时出现时被标为相同隐私级别的次数
		self.coLevel = np.zeros((len(self.scene_dict),len(self.object_dict),len(self.object_dict)), dtype='uint16')
		# level[s][i][j]表示scene s中object i被判定为level j的可能性
		self.level=np.ones((len(self.scene_dict),len(self.object_dict),n+1),dtype='float32')

	def returnLevel(self, scene, object_list):
		#返回图片中每一个object对应的隐私级别
		#scene为图片对应的scene_class
		#object_list为检测出的所有object_class,格式为[object_class,object_class,...]
		#返回一个字典，标明各object_class对应的隐私级别，格式为{object_class:level,..}
		result={}
		scene_id=self.scene_dict[scene]
		for i in object_list:
			result[i]=np.argmax(self.level[scene_id][self.object_dict[i]])
		return result

		
	def updateLevel(self, scene, userSetLevel):
		#问询一张图片，得到用户反馈后调用，更新隐私级别，无返回值
		#scene为该图片的scene_class
		#userSetLevel是一个字典，格式为{'object_class':level,...}
		#这里假设图中同一类object的隐私级别相同，同一张图中出现多个相同类别的object时，仅计算1次

		#问询图片数加1
		self.imgNum += 1
		scene_id=self.scene_dict[scene]
		tmp=[]
		oid_level={}
		#统计各object class在所有隐私级别上的权值之和
		level_sum=np.sum(self.level,axis=2)
		for i in userSetLevel:
			tmp.append(self.object_dict[i]) #存储对象id
			oid_level[self.object_dict[i]]=userSetLevel[i] #构建id-level对应关系
			self.singleAppear[scene_id][self.object_dict[i]]+=1 #object出现次数加1
			#更新该object在各level上的权值
			mid = (level_sum[scene_id][self.object_dict[i]]-self.level[scene_id][self.object_dict[i]][userSetLevel[i]])/self.max_level
			self.level[scene_id][self.object_dict[i]][userSetLevel[i]]+=mid
			for res in range(self.max_level+1):
				if res!=userSetLevel[i]:
					self.level[scene_id][self.object_dict[i]][res]*=((self.max_level-1)/self.max_level)
		for i in range(len(tmp)-1):
			for j in range(i+1,len(tmp)):
				self.coAppear[scene_id][tmp[i]][tmp[j]]+=1 # 两object同时出现次数加1
				self.coAppear[scene_id][tmp[j]][tmp[i]]+=1
				if oid_level[tmp[i]]==oid_level[tmp[j]]:
					self.coLevel[scene_id][tmp[i]][tmp[j]]+=1 #两object被设置为相同隐私级别次数加1
					self.coLevel[scene_id][tmp[j]][tmp[i]]+=1
		#更新其余所有类别的object的权值
		for i in userSetLevel:
			for j in self.object_dict:
				if j in userSetLevel:					
					pass
				elif self.coAppear[scene_id][self.object_dict[i]][self.object_dict[j]]!=0 and self.coLevel[scene_id][self.object_dict[i]][self.object_dict[j]]!=0:
					#计算i,j同时出现概率
					p_i_j = self.coAppear[scene_id][self.object_dict[i]][self.object_dict[j]]/self.imgNum
					p_i = self.singleAppear[scene_id][self.object_dict[i]]/self.imgNum
					p_j = self.singleAppear[scene_id][self.object_dict[j]]/self.imgNum
					p = -p_i_j*np.log(p_i_j/(p_i+p_j))
					u = self.coLevel[scene_id][self.object_dict[i]][self.object_dict[j]]/self.coAppear[scene_id][self.object_dict[i]][self.object_dict[j]]
					for k in range(self.max_level+1):
						self.level[scene_id][self.object_dict[j]][k]=self.level[scene_id][self.object_dict[j]][k]*(1-self.learning_rate)+self.learning_rate*p*u*self.level[scene_id][self.object_dict[i]][k]
