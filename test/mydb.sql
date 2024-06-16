-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `buyer`
--

DROP TABLE IF EXISTS `buyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buyer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(300) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `Platform_id` int NOT NULL,
  `Genre_id` int NOT NULL,
  `boughtgames` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_Buyer_Platform1_idx` (`Platform_id`),
  KEY `fk_Buyer_Genre1_idx` (`Genre_id`),
  CONSTRAINT `fk_Buyer_Genre1` FOREIGN KEY (`Genre_id`) REFERENCES `genre` (`id`),
  CONSTRAINT `fk_Buyer_Platform1` FOREIGN KEY (`Platform_id`) REFERENCES `platform` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyer`
--

LOCK TABLES `buyer` WRITE;
/*!40000 ALTER TABLE `buyer` DISABLE KEYS */;
INSERT INTO `buyer` VALUES (1,'Павел','Katya1926','1990-01-01',4,12,0),(2,'Игорь','Oleg2345','1995-07-15',5,1,0),(3,'Сергей','Yana_927','1985-09-25',6,5,0),(4,'Алина','Yuri_1987','1998-05-12',3,4,0),(5,'Виктор','Yulia_1998','1991-09-20',1,21,0),(6,'Ирина','Yana_927','1992-11-03',2,20,1),(7,'Иван','Yuri_1987','1985-09-25',7,19,0),(8,'Кирилл','Yulia_1998','1998-05-12',8,3,0),(9,'Тимур','Yana_927','2001-04-15',9,2,0),(10,'Ильназ','Yuri_1987','1973-12-12',12,2,0),(11,'Егор','ыфорафыо','2013-12-12',1,3,0);
/*!40000 ALTER TABLE `buyer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `developer`
--

DROP TABLE IF EXISTS `developer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `developer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(45) DEFAULT NULL,
  `user_rating` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `developer`
--

LOCK TABLES `developer` WRITE;
/*!40000 ALTER TABLE `developer` DISABLE KEYS */;
INSERT INTO `developer` VALUES (1,'Electronic Arts',2),(2,'Gearbox',4),(3,'Nintendo',5),(4,'Sony Interactive  Entertainment',5),(5,'Xbox Game Studios',5),(6,'Devolver Digital',5),(7,'Valve',5),(8,'2K Games',3),(9,'Activision Blizzard',1),(10,'Arc System Works',5),(11,'Embracer Group',4),(12,'Sega',4),(13,'Capcom',4),(14,'CD Projekt RED',5),(15,'Epic Games',4),(16,'Focus Entertainment',4),(17,'Square Enix',4),(18,'Konami',2),(19,'Paradox Interactive',5),(20,'Riot Games',4);
/*!40000 ALTER TABLE `developer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(45) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Александр','1992-03-17'),(2,'Иван','2001-08-29'),(3,'Дмитрий','1995-12-05'),(4,'Сергей','1998-06-14'),(5,'Анастасия','2005-04-22'),(6,'Мария','1996-11-08'),(7,'София','2012-07-31'),(8,'Алексей','2008-05-10'),(9,'Анна','1990-02-24'),(10,'Екатерина','2018-09-26');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(45) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `age_rating` int DEFAULT NULL,
  `user_rating` float DEFAULT '0',
  `release_date` date DEFAULT NULL,
  `player_count` int DEFAULT NULL,
  `language` varchar(45) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `Platform_id` int NOT NULL,
  `Genre_id` int NOT NULL,
  `Developer_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Game_Platform1_idx` (`Platform_id`),
  KEY `fk_Game_Genre1_idx` (`Genre_id`),
  KEY `fk_Game_Developer1_idx` (`Developer_id`),
  CONSTRAINT `fk_Game_Developer1` FOREIGN KEY (`Developer_id`) REFERENCES `developer` (`id`),
  CONSTRAINT `fk_Game_Genre1` FOREIGN KEY (`Genre_id`) REFERENCES `genre` (`id`),
  CONSTRAINT `fk_Game_Platform1` FOREIGN KEY (`Platform_id`) REFERENCES `platform` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'Super Mario Wonder',60,0,5,'2023-10-20',4,'English',103100,5,16,3),(2,'Super Smash Bros. Ultimate',60,10,5,'2018-12-07',8,'English, Russian',200000,5,10,3),(3,'Guilty Gear - Strive-',40,18,4.9,'2021-07-11',2,'English',49999,4,10,10),(4,'Xenoblade Chronicles 3',60,12,5,'2022-07-29',1,'English',1000000,5,6,3),(5,'Spider-Man 2',70,12,4.5,'2023-10-20',1,'English',2000000,4,7,4),(6,'Starfield',70,18,3.6,'2023-09-06',1,'English',102000,3,6,5),(7,'Overwatch 2',30,16,0,'2023-08-10',1,'English, Russian',200000,3,1,9),(8,'Overwatch 2',30,16,0,'2023-08-10',1,'English, Russian',200000,4,1,9),(9,'Overwatch 2',30,16,0,'2023-08-10',1,'English, Russian',200000,6,1,9),(10,'Overwatch 2',30,16,0,'2023-08-10',1,'English, Russian',200000,5,1,9);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'FPS'),(2,'RTS'),(3,'TBS'),(4,'Racing'),(5,'Immersive Sim'),(6,'RPG'),(7,'Action-Adventure'),(8,'Puzzle'),(9,'TPS'),(10,'Fighting'),(11,'Sports'),(12,'Flight'),(13,'Horror'),(14,'Rogue-Like'),(15,'Souls-Like'),(16,'Platformer'),(17,'Metroidvania'),(18,'Rhythm Game'),(19,'Hack and Slash'),(20,'Visual Novel'),(21,'Beat \'Em Up');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platform`
--

DROP TABLE IF EXISTS `platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platform` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platform`
--

LOCK TABLES `platform` WRITE;
/*!40000 ALTER TABLE `platform` DISABLE KEYS */;
INSERT INTO `platform` VALUES (1,'Microsoft Xbox One'),(2,'Sony Playstation 4'),(3,'Microsoft Xbox Series'),(4,'Sony Playstation 5'),(5,'Nintendo Switch'),(6,'PC'),(7,'Microsoft Xbox 360'),(8,'Sony Playstation 3'),(9,'Nintendo WiiU'),(10,'Nintendo Wii'),(11,'Nintendo 3DS'),(12,'Nintendo DS'),(13,'Sony Playstation Vita'),(14,'Sony Playstation Portable');
/*!40000 ALTER TABLE `platform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dates` date DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `Game_id` int NOT NULL,
  `Employee_id` int NOT NULL,
  `Buyer_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Purchase_Game1_idx` (`Game_id`),
  KEY `fk_Purchase_Employee1_idx` (`Employee_id`),
  KEY `fk_Purchase_Buyer1_idx` (`Buyer_id`),
  CONSTRAINT `fk_Purchase_Buyer1` FOREIGN KEY (`Buyer_id`) REFERENCES `buyer` (`id`),
  CONSTRAINT `fk_Purchase_Employee1` FOREIGN KEY (`Employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `fk_Purchase_Game1` FOREIGN KEY (`Game_id`) REFERENCES `game` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1,'2023-10-23',1,1,1,6),(2,'2023-10-22',2,3,5,7),(3,'2023-10-21',1,4,6,2),(4,'2023-10-20',1,2,8,8),(5,'2023-10-23',2,5,10,4),(6,'2023-10-20',1,3,2,6),(7,'2023-10-21',3,4,3,7),(8,'2023-10-21',1,4,4,8),(9,'2023-10-21',1,5,5,9),(10,'2023-10-21',3,2,7,10),(11,'2023-11-12',2,1,5,6);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `purchase_BEFORE_INSERT` BEFORE INSERT ON `purchase` FOR EACH ROW BEGIN
declare stock_after_purchase int;
declare buyer_birthdate date;
declare buyer_age int;
declare game_age_rating int;
select game.stock-new.amount into stock_after_purchase from game where game.id=new.Game_id;
if stock_after_purchase <0 then
	signal sqlstate '45001' set MESSAGE_TEXT = 'Недостаточно игр на складе'; 
else
select game.age_rating into game_age_rating from game where new.Game_id=game.id;
select buyer.birth_date into buyer_birthdate from buyer where new.Buyer_id=buyer.id;
SET buyer_age = DATEDIFF(curdate(),buyer_birthdate);
if buyer_age/365<game_age_rating then
	signal sqlstate '45000' set MESSAGE_TEXT = 'Возраст покупателя ниже возрастного рейтинга игры'; 
end if;
end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `purchase_AFTER_INSERT` AFTER INSERT ON `purchase` FOR EACH ROW BEGIN
update buyer set boughtgames=boughtgames+1 where buyer.id=new.Buyer_id;
update game set stock=stock-new.amount where new.Game_id=game.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `purchase_AFTER_DELETE` AFTER DELETE ON `purchase` FOR EACH ROW BEGIN
update buyer set boughtgames=boughtgames-old.amount where buyer.id=old.Buyer_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `количество`
--

DROP TABLE IF EXISTS `количество`;
/*!50001 DROP VIEW IF EXISTS `количество`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `количество` AS SELECT 
 1 AS `count(*)`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `количество`
--

/*!50001 DROP VIEW IF EXISTS `количество`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `количество` AS select count(0) AS `count(*)` from `game` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-16 16:53:40
