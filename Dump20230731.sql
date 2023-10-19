-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ccsitv_flyfishers
-- ------------------------------------------------------
-- Server version	5.7.40-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alert`
--

DROP TABLE IF EXISTS `alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alert` (
  `alert_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`alert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alert`
--

LOCK TABLES `alert` WRITE;
/*!40000 ALTER TABLE `alert` DISABLE KEYS */;
INSERT INTO `alert` VALUES (1,'2023-07-28','gjig'),(2,'2023-07-28','nbmbm');
/*!40000 ALTER TABLE `alert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add alert',7,'add_alert'),(26,'Can change alert',7,'change_alert'),(27,'Can delete alert',7,'delete_alert'),(28,'Can view alert',7,'view_alert'),(29,'Can add compensation',8,'add_compensation'),(30,'Can change compensation',8,'change_compensation'),(31,'Can delete compensation',8,'delete_compensation'),(32,'Can view compensation',8,'view_compensation'),(33,'Can add deputydirector',9,'add_deputydirector'),(34,'Can change deputydirector',9,'change_deputydirector'),(35,'Can delete deputydirector',9,'delete_deputydirector'),(36,'Can view deputydirector',9,'view_deputydirector'),(37,'Can add educational assistance',10,'add_educationalassistance'),(38,'Can change educational assistance',10,'change_educationalassistance'),(39,'Can delete educational assistance',10,'delete_educationalassistance'),(40,'Can view educational assistance',10,'view_educationalassistance'),(41,'Can add equipment',11,'add_equipment'),(42,'Can change equipment',11,'change_equipment'),(43,'Can delete equipment',11,'delete_equipment'),(44,'Can view equipment',11,'view_equipment'),(45,'Can add fisheries officer',12,'add_fisheriesofficer'),(46,'Can change fisheries officer',12,'change_fisheriesofficer'),(47,'Can delete fisheries officer',12,'delete_fisheriesofficer'),(48,'Can view fisheries officer',12,'view_fisheriesofficer'),(49,'Can add fishermen',13,'add_fishermen'),(50,'Can change fishermen',13,'change_fishermen'),(51,'Can delete fishermen',13,'delete_fishermen'),(52,'Can view fishermen',13,'view_fishermen'),(53,'Can add freenet licence',14,'add_freenetlicence'),(54,'Can change freenet licence',14,'change_freenetlicence'),(55,'Can delete freenet licence',14,'delete_freenetlicence'),(56,'Can view freenet licence',14,'view_freenetlicence'),(57,'Can add insurance',15,'add_insurance'),(58,'Can change insurance',15,'change_insurance'),(59,'Can delete insurance',15,'delete_insurance'),(60,'Can view insurance',15,'view_insurance'),(61,'Can add login',16,'add_login'),(62,'Can change login',16,'change_login'),(63,'Can delete login',16,'delete_login'),(64,'Can view login',16,'view_login'),(65,'Can add order',17,'add_order'),(66,'Can change order',17,'change_order'),(67,'Can delete order',17,'delete_order'),(68,'Can view order',17,'view_order'),(69,'Can add payment',18,'add_payment'),(70,'Can change payment',18,'change_payment'),(71,'Can delete payment',18,'delete_payment'),(72,'Can view payment',18,'view_payment'),(73,'Can add vessel license',19,'add_vessellicense'),(74,'Can change vessel license',19,'change_vessellicense'),(75,'Can delete vessel license',19,'delete_vessellicense'),(76,'Can view vessel license',19,'view_vessellicense'),(77,'Can add prawn filtration',20,'add_prawnfiltration'),(78,'Can change prawn filtration',20,'change_prawnfiltration'),(79,'Can delete prawn filtration',20,'delete_prawnfiltration'),(80,'Can view prawn filtration',20,'view_prawnfiltration'),(81,'Can add relief schem',21,'add_reliefschem'),(82,'Can change relief schem',21,'change_reliefschem'),(83,'Can delete relief schem',21,'delete_reliefschem'),(84,'Can view relief schem',21,'view_reliefschem'),(85,'Can add req compensation',22,'add_reqcompensation'),(86,'Can change req compensation',22,'change_reqcompensation'),(87,'Can delete req compensation',22,'delete_reqcompensation'),(88,'Can view req compensation',22,'view_reqcompensation'),(89,'Can add req vessel license',23,'add_reqvessellicense'),(90,'Can change req vessel license',23,'change_reqvessellicense'),(91,'Can delete req vessel license',23,'delete_reqvessellicense'),(92,'Can view req vessel license',23,'view_reqvessellicense'),(93,'Can add req freenet license',24,'add_reqfreenetlicense'),(94,'Can change req freenet license',24,'change_reqfreenetlicense'),(95,'Can delete req freenet license',24,'delete_reqfreenetlicense'),(96,'Can view req freenet license',24,'view_reqfreenetlicense'),(97,'Can add req insurance',25,'add_reqinsurance'),(98,'Can change req insurance',25,'change_reqinsurance'),(99,'Can delete req insurance',25,'delete_reqinsurance'),(100,'Can view req insurance',25,'view_reqinsurance'),(101,'Can add req prawn filtration',26,'add_reqprawnfiltration'),(102,'Can change req prawn filtration',26,'change_reqprawnfiltration'),(103,'Can delete req prawn filtration',26,'delete_reqprawnfiltration'),(104,'Can view req prawn filtration',26,'view_reqprawnfiltration'),(105,'Can add req relief scheme',27,'add_reqreliefscheme'),(106,'Can change req relief scheme',27,'change_reqreliefscheme'),(107,'Can delete req relief scheme',27,'delete_reqreliefscheme'),(108,'Can view req relief scheme',27,'view_reqreliefscheme'),(109,'Can add student',28,'add_student'),(110,'Can change student',28,'change_student'),(111,'Can delete student',28,'delete_student'),(112,'Can view student',28,'view_student'),(113,'Can add trolling',29,'add_trolling'),(114,'Can change trolling',29,'change_trolling'),(115,'Can delete trolling',29,'delete_trolling'),(116,'Can view trolling',29,'view_trolling'),(117,'Can add vessel',30,'add_vessel'),(118,'Can change vessel',30,'change_vessel'),(119,'Can delete vessel',30,'delete_vessel'),(120,'Can view vessel',30,'view_vessel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compensation`
--

DROP TABLE IF EXISTS `compensation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compensation` (
  `compensation_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `amount` int(11) NOT NULL,
  `rules` varchar(200) NOT NULL,
  PRIMARY KEY (`compensation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compensation`
--

LOCK TABLES `compensation` WRITE;
/*!40000 ALTER TABLE `compensation` DISABLE KEYS */;
INSERT INTO `compensation` VALUES (1,'com',900,'compensation.pdf'),(2,'com',900,'compensation.pdf'),(3,'fghhj',10200,'vessel verification.pdf');
/*!40000 ALTER TABLE `compensation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deputydirector`
--

DROP TABLE IF EXISTS `deputydirector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deputydirector` (
  `deputydirector_id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `date of birth` date NOT NULL,
  `gender` varchar(45) NOT NULL,
  `qualification` varchar(45) NOT NULL,
  `pincode` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `district` varchar(45) NOT NULL,
  `contact no` varchar(20) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`deputydirector_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deputydirector`
--

LOCK TABLES `deputydirector` WRITE;
/*!40000 ALTER TABLE `deputydirector` DISABLE KEYS */;
INSERT INTO `deputydirector` VALUES (2,'Archana ','2023-07-27','Female','P H D','673506','kallachi','hjhjko','4545454787','archananm@gmail.com','123'),(3,'anu     ','2023-07-31','Male','P H D','4152369874','kallachi','pppp','4152369874','anu@gmail.com','anu');
/*!40000 ALTER TABLE `deputydirector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'alert','alert'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'compensation','compensation'),(5,'contenttypes','contenttype'),(9,'deputydirector','deputydirector'),(10,'education_assistance','educationalassistance'),(11,'equipment','equipment'),(12,'fisheries_officer','fisheriesofficer'),(13,'fishermen','fishermen'),(14,'freenet_license','freenetlicence'),(15,'insurance','insurance'),(16,'login','login'),(17,'orders','order'),(18,'payment','payment'),(20,'prawn_filtration','prawnfiltration'),(21,'relief_scheme','reliefschem'),(22,'request_compensation','reqcompensation'),(24,'request_freenet_license','reqfreenetlicense'),(25,'request_insurance','reqinsurance'),(26,'request_prawn_filtration','reqprawnfiltration'),(27,'request_releif_scheme','reqreliefscheme'),(23,'request_vessel_license','reqvessellicense'),(6,'sessions','session'),(28,'student','student'),(29,'trolling','trolling'),(30,'vessel','vessel'),(19,'vessel_license','vessellicense');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-07-19 07:23:25.999082'),(2,'auth','0001_initial','2023-07-19 07:23:26.697010'),(3,'admin','0001_initial','2023-07-19 07:23:26.852710'),(4,'admin','0002_logentry_remove_auto_add','2023-07-19 07:23:26.861884'),(5,'admin','0003_logentry_add_action_flag_choices','2023-07-19 07:23:26.870881'),(6,'alert','0001_initial','2023-07-19 07:23:26.876939'),(7,'contenttypes','0002_remove_content_type_name','2023-07-19 07:23:26.971381'),(8,'auth','0002_alter_permission_name_max_length','2023-07-19 07:23:27.004417'),(9,'auth','0003_alter_user_email_max_length','2023-07-19 07:23:27.041071'),(10,'auth','0004_alter_user_username_opts','2023-07-19 07:23:27.056604'),(11,'auth','0005_alter_user_last_login_null','2023-07-19 07:23:27.115410'),(12,'auth','0006_require_contenttypes_0002','2023-07-19 07:23:27.124027'),(13,'auth','0007_alter_validators_add_error_messages','2023-07-19 07:23:27.142240'),(14,'auth','0008_alter_user_username_max_length','2023-07-19 07:23:27.180529'),(15,'auth','0009_alter_user_last_name_max_length','2023-07-19 07:23:27.217791'),(16,'auth','0010_alter_group_name_max_length','2023-07-19 07:23:27.254903'),(17,'auth','0011_update_proxy_permissions','2023-07-19 07:23:27.270167'),(18,'auth','0012_alter_user_first_name_max_length','2023-07-19 07:23:27.297170'),(19,'compensation','0001_initial','2023-07-19 07:23:27.305169'),(20,'deputydirector','0001_initial','2023-07-19 07:23:27.311339'),(21,'education_assistance','0001_initial','2023-07-19 07:23:27.319647'),(22,'equipment','0001_initial','2023-07-19 07:23:27.326646'),(23,'fisheries_officer','0001_initial','2023-07-19 07:23:27.333030'),(24,'fishermen','0001_initial','2023-07-19 07:23:27.339964'),(25,'freenet_license','0001_initial','2023-07-19 07:23:27.347336'),(26,'insurance','0001_initial','2023-07-19 07:23:27.353332'),(27,'login','0001_initial','2023-07-19 07:23:27.358901'),(28,'orders','0001_initial','2023-07-19 07:23:27.368590'),(29,'payment','0001_initial','2023-07-19 07:23:27.374813'),(30,'prawn_filtration','0001_initial','2023-07-19 07:23:27.382737'),(31,'relief_scheme','0001_initial','2023-07-19 07:23:27.389461'),(32,'request_compensation','0001_initial','2023-07-19 07:23:27.397708'),(33,'request_freenet_license','0001_initial','2023-07-19 07:23:27.404277'),(34,'request_insurance','0001_initial','2023-07-19 07:23:27.412044'),(35,'request_prawn_filtration','0001_initial','2023-07-19 07:23:27.418788'),(36,'request_releif_scheme','0001_initial','2023-07-19 07:23:27.425155'),(37,'request_vessel_license','0001_initial','2023-07-19 07:23:27.433618'),(38,'sessions','0001_initial','2023-07-19 07:23:27.487302'),(39,'student','0001_initial','2023-07-19 07:23:27.494890'),(40,'trolling','0001_initial','2023-07-19 07:23:27.501064'),(41,'vessel','0001_initial','2023-07-19 07:23:27.509732'),(42,'vessel_license','0001_initial','2023-07-19 07:23:27.516896');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('f23x4sd11km3dpknc06hixo4mf2cc33y','eyJ1X2lkIjoxfQ:1qQOx8:yIDfO_FJ6MuKFrwRX_NjISZTbraI-AjFAe35589Jwas','2023-08-14 09:12:34.126605');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `educational_assistance`
--

DROP TABLE IF EXISTS `educational_assistance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `educational_assistance` (
  `educational_assistance_id` int(11) NOT NULL AUTO_INCREMENT,
  `scolarship name` varchar(45) NOT NULL,
  `description` varchar(300) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`educational_assistance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `educational_assistance`
--

LOCK TABLES `educational_assistance` WRITE;
/*!40000 ALTER TABLE `educational_assistance` DISABLE KEYS */;
INSERT INTO `educational_assistance` VALUES (1,'nnbmvb','vessel verification.pdf','Pending');
/*!40000 ALTER TABLE `educational_assistance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `equipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `equipment name` varchar(45) NOT NULL,
  `equipmentimage` varchar(500) NOT NULL,
  `quandity` int(11) NOT NULL,
  `subsidy` varchar(45) NOT NULL,
  `price` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1,'net','pexels-quang-nguyen-vinh-6876904.jpg',45,'454',451,'Pending',1),(2,'bjb','pexels-quang-nguyen-vinh-2131945.jpg',41,'11',100,'Pending',1);
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fisheries_officer`
--

DROP TABLE IF EXISTS `fisheries_officer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fisheries_officer` (
  `fisheries_officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `date of birth` date NOT NULL,
  `gender` varchar(45) NOT NULL,
  `qualification` varchar(45) NOT NULL,
  `pincode` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `district` varchar(45) NOT NULL,
  `contact no` varchar(30) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`fisheries_officer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fisheries_officer`
--

LOCK TABLES `fisheries_officer` WRITE;
/*!40000 ALTER TABLE `fisheries_officer` DISABLE KEYS */;
INSERT INTO `fisheries_officer` VALUES (2,'Saniya','2023-07-28','Female','phd','546112','vadmnm','aaaaaahjkvbm','2415555455','sani@gmail.com','456');
/*!40000 ALTER TABLE `fisheries_officer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishermen`
--

DROP TABLE IF EXISTS `fishermen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fishermen` (
  `fishermen_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `date of birth` date NOT NULL,
  `gender` varchar(45) NOT NULL,
  `qualification` varchar(45) NOT NULL,
  `pincode` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `district` varchar(45) NOT NULL,
  `contact` varchar(30) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `id_proof` varchar(200) NOT NULL,
  PRIMARY KEY (`fishermen_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishermen`
--

LOCK TABLES `fishermen` WRITE;
/*!40000 ALTER TABLE `fishermen` DISABLE KEYS */;
INSERT INTO `fishermen` VALUES (1,'revi','2023-07-27','Male','sslc','673506','dsfbnfmd','bdnmnfm','4512664878','revi@gmail.com','revi',''),(2,'rajan','2023-07-29','Male','8','673014','vadakara','mnmm','4511541478','raj@gmail.com','741','compensation.pdf'),(3,'arvn','2023-07-31','Male','plus two','673506','vadmn','hvhv','2112124545','ar@gmail.com','1425','compensation.pdf');
/*!40000 ALTER TABLE `fishermen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `freenet_licence`
--

DROP TABLE IF EXISTS `freenet_licence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `freenet_licence` (
  `freenet_licence_id` int(11) NOT NULL AUTO_INCREMENT,
  `type of net` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`freenet_licence_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `freenet_licence`
--

LOCK TABLES `freenet_licence` WRITE;
/*!40000 ALTER TABLE `freenet_licence` DISABLE KEYS */;
INSERT INTO `freenet_licence` VALUES (1,'jbnnm','Fishing vessels- licencing.pdf'),(2,'hhj','vessel verification.pdf');
/*!40000 ALTER TABLE `freenet_licence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insurance`
--

DROP TABLE IF EXISTS `insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insurance` (
  `insurance_id` int(11) NOT NULL AUTO_INCREMENT,
  `insurance name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`insurance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurance`
--

LOCK TABLES `insurance` WRITE;
/*!40000 ALTER TABLE `insurance` DISABLE KEYS */;
INSERT INTO `insurance` VALUES (1,'insurance1','Fishing vessels- licencing.pdf'),(2,'insu','education.pdf'),(3,'insupp','vessel verification.pdf');
/*!40000 ALTER TABLE `insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'admin','admin','director',1),(2,'Archana','123','deputy_director',1),(3,'Anagha','456','fisheries_officer',1),(4,'Archana ','123','deputy_director',2),(5,'anu','anu','deputy_director',3),(6,'revi','revi','fishermen',1),(7,'Saniya','456','fisheries_officer',2),(8,'rajan','741','fishermen',2),(9,'arvn','1425','fishermen',3),(10,'ghgh','vvh','deputy_director',4);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `equipment_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `quantity` varchar(45) NOT NULL,
  `amount` varchar(45) NOT NULL,
  `subcidy` varchar(45) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,2,1,'Approved','1','100','11'),(2,2,1,'ordered','1','100','11'),(3,2,1,'ordered','4','400','11'),(4,2,1,'ordered','2','200','11'),(5,2,1,'ordered','2','200','11'),(6,2,1,'ordered','2','200','11'),(7,2,1,'ordered','2','200','11'),(8,2,1,'ordered','2','200','11'),(9,2,1,'ordered','5','500','11'),(10,2,1,'ordered','5','500','11'),(11,2,1,'Approved','5','500','11'),(12,2,1,'Approved','4','400','11'),(13,2,1,'ordered','4','400','11'),(14,2,1,'ordered','4','400','11'),(15,2,1,'ordered','4','400','11'),(16,2,1,'ordered','1','89','11');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `fishermen_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `account no` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `bank name` varchar(45) NOT NULL,
  `branch name` varchar(45) NOT NULL,
  `ifsc code` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,1,1,'revi',897654,100,'sbi','jhh','jg09','Paid');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prawn_filtration`
--

DROP TABLE IF EXISTS `prawn_filtration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prawn_filtration` (
  `prawn_filtration_id` int(11) NOT NULL AUTO_INCREMENT,
  `available date` varchar(45) NOT NULL,
  `Details` varchar(500) NOT NULL,
  PRIMARY KEY (`prawn_filtration_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prawn_filtration`
--

LOCK TABLES `prawn_filtration` WRITE;
/*!40000 ALTER TABLE `prawn_filtration` DISABLE KEYS */;
INSERT INTO `prawn_filtration` VALUES (1,'2023-08-22','Register for prawn filtration licence.pdf'),(2,'2023-08-22','vessel verification.pdf');
/*!40000 ALTER TABLE `prawn_filtration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relief_schem`
--

DROP TABLE IF EXISTS `relief_schem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relief_schem` (
  `relief_schem_id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  PRIMARY KEY (`relief_schem_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relief_schem`
--

LOCK TABLES `relief_schem` WRITE;
/*!40000 ALTER TABLE `relief_schem` DISABLE KEYS */;
INSERT INTO `relief_schem` VALUES (1,'relief1','relief scheme 1.pdf'),(2,'relief2','relief scheme 2.pdf'),(3,'relief3','relief scheme 3.pdf'),(4,'relief4','relief scheme 4.pdf'),(5,'relief5','relief scheme 4.pdf'),(6,'relief6','relief scheme 3.pdf'),(7,'recg','relief scheme 1.pdf');
/*!40000 ALTER TABLE `relief_schem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_compensation`
--

DROP TABLE IF EXISTS `req_compensation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_compensation` (
  `req_compensation_id` int(11) NOT NULL AUTO_INCREMENT,
  `compensation_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `user name` varchar(45) NOT NULL,
  `reason` varchar(45) NOT NULL,
  `proof` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(45) NOT NULL,
  `details` varchar(400) NOT NULL,
  PRIMARY KEY (`req_compensation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_compensation`
--

LOCK TABLES `req_compensation` WRITE;
/*!40000 ALTER TABLE `req_compensation` DISABLE KEYS */;
INSERT INTO `req_compensation` VALUES (1,1,1,'saniya','dwfk','compensation.pdf','2023-07-12','pending','vessel verification.pdf'),(2,1,1,'revi','dwfk','compensation.pdf','2023-07-12','Approved','vessel verification.pdf'),(3,1,1,'revi','msbam','compensation.pdf','2023-07-12','Approved','compensation.pdf');
/*!40000 ALTER TABLE `req_compensation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_freenet_license`
--

DROP TABLE IF EXISTS `req_freenet_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_freenet_license` (
  `req_freenet_license_id` int(11) NOT NULL AUTO_INCREMENT,
  `fishermen_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(45) NOT NULL,
  `freenet_licence_id` int(11) NOT NULL,
  `id_proof` varchar(45) NOT NULL,
  `more_details` varchar(400) NOT NULL,
  PRIMARY KEY (`req_freenet_license_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_freenet_license`
--

LOCK TABLES `req_freenet_license` WRITE;
/*!40000 ALTER TABLE `req_freenet_license` DISABLE KEYS */;
INSERT INTO `req_freenet_license` VALUES (1,1,'2023-07-28','Approved',1,'compensation.pdf','compensation.pdf'),(2,1,'2023-07-28','Requested',1,'compensation.pdf','compensation.pdf'),(3,1,'2023-07-31','Requested',1,'compensation.pdf','compensation.pdf');
/*!40000 ALTER TABLE `req_freenet_license` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_insurance`
--

DROP TABLE IF EXISTS `req_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_insurance` (
  `req_insurance_id` int(11) NOT NULL AUTO_INCREMENT,
  `insurance_id` int(11) NOT NULL,
  `vessel_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `id_proof` varchar(45) NOT NULL,
  PRIMARY KEY (`req_insurance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_insurance`
--

LOCK TABLES `req_insurance` WRITE;
/*!40000 ALTER TABLE `req_insurance` DISABLE KEYS */;
INSERT INTO `req_insurance` VALUES (1,1,1,1,'Approved','package-3.jpg'),(2,1,1,1,'Requested','compensation.pdf');
/*!40000 ALTER TABLE `req_insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_prawn_filtration`
--

DROP TABLE IF EXISTS `req_prawn_filtration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_prawn_filtration` (
  `req_prawn_filtration_id` int(11) NOT NULL AUTO_INCREMENT,
  `prawn_filtration_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `license no` int(11) NOT NULL,
  `request` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`req_prawn_filtration_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_prawn_filtration`
--

LOCK TABLES `req_prawn_filtration` WRITE;
/*!40000 ALTER TABLE `req_prawn_filtration` DISABLE KEYS */;
INSERT INTO `req_prawn_filtration` VALUES (1,1,1,111,'compensation.pdf','2023-07-28','Approved'),(2,1,1,67890,'compensation.pdf','2023-07-31','requested'),(3,1,1,67890,'compensation.pdf','2023-07-31','requested');
/*!40000 ALTER TABLE `req_prawn_filtration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_relief_scheme`
--

DROP TABLE IF EXISTS `req_relief_scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_relief_scheme` (
  `req_relief_schem_id` int(11) NOT NULL AUTO_INCREMENT,
  `relief_schem_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `id proof` varchar(45) NOT NULL,
  PRIMARY KEY (`req_relief_schem_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_relief_scheme`
--

LOCK TABLES `req_relief_scheme` WRITE;
/*!40000 ALTER TABLE `req_relief_scheme` DISABLE KEYS */;
INSERT INTO `req_relief_scheme` VALUES (1,1,1,'Approved','relief scheme 1.pdf'),(2,1,1,'Approved','relief scheme 3.pdf'),(3,1,1,'Rejected','relief scheme 1.pdf'),(4,3,1,'Approved','relief scheme 1.pdf'),(5,7,1,'Requested','compensation.pdf');
/*!40000 ALTER TABLE `req_relief_scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `req_vessel_license`
--

DROP TABLE IF EXISTS `req_vessel_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `req_vessel_license` (
  `req_vessel_license_id` int(11) NOT NULL AUTO_INCREMENT,
  `vessel_license_id` int(11) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `vessel no` int(11) NOT NULL,
  `request` varchar(45) NOT NULL,
  `id proof` varchar(45) NOT NULL,
  `manifacture date` date NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`req_vessel_license_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `req_vessel_license`
--

LOCK TABLES `req_vessel_license` WRITE;
/*!40000 ALTER TABLE `req_vessel_license` DISABLE KEYS */;
INSERT INTO `req_vessel_license` VALUES (1,1,1,'revi',1111,'kjkflbj','vessel verification.pdf','2023-07-10','Approved'),(2,1,1,'boat',111,'cghgj','Registration Form vessel.pdf','2023-07-10','requested'),(3,1,1,'boat',111,'cghgj','Registration Form vessel.pdf','2023-07-10','requested');
/*!40000 ALTER TABLE `req_vessel_license` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `student name` varchar(45) NOT NULL,
  `student class` int(11) NOT NULL,
  `date of birth` date NOT NULL,
  `village` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `pin code` int(11) NOT NULL,
  `district` varchar(45) NOT NULL,
  `institution` varchar(45) NOT NULL,
  `mark` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `educational_assistance_id` varchar(45) NOT NULL,
  `fishermen_id` int(11) NOT NULL,
  `fishermen_id_proof` varchar(400) NOT NULL,
  `relation proof` varchar(400) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'sabikcsn',10,'2023-07-28','bmbnm','bjhb',545412,' nbmb','gjhkh','compensation.pdf','Approved','1',1,'compensation.pdf','compensation.pdf'),(2,'vhbjnk',10,'2023-07-31','vhjkl','vadakara',673015,' m mnm','nnn','compensation.pdf','Requested','1',1,'compensation.pdf','compensation.pdf');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trolling`
--

DROP TABLE IF EXISTS `trolling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trolling` (
  `trolling_id` int(11) NOT NULL AUTO_INCREMENT,
  `trolling info` varchar(200) NOT NULL,
  `starting date` date NOT NULL,
  `ending date` date NOT NULL,
  PRIMARY KEY (`trolling_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trolling`
--

LOCK TABLES `trolling` WRITE;
/*!40000 ALTER TABLE `trolling` DISABLE KEYS */;
INSERT INTO `trolling` VALUES (1,'relief scheme 1.pdf','2023-07-28','2023-07-28');
/*!40000 ALTER TABLE `trolling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vessel`
--

DROP TABLE IF EXISTS `vessel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vessel` (
  `vessel_id` int(11) NOT NULL AUTO_INCREMENT,
  `fishermen_id` int(11) NOT NULL,
  `fishermen name` varchar(45) NOT NULL,
  `name of vessel` varchar(45) NOT NULL,
  `register no` int(11) NOT NULL,
  `license no` int(11) NOT NULL,
  `crew` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `register date` date NOT NULL,
  `register place` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `detailed_description` varchar(400) NOT NULL,
  PRIMARY KEY (`vessel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vessel`
--

LOCK TABLES `vessel` WRITE;
/*!40000 ALTER TABLE `vessel` DISABLE KEYS */;
INSERT INTO `vessel` VALUES (1,1,'revi','boat',111,101,50,2010,'2023-08-12','palakad','Verified',''),(2,1,'revi','canoe',101,101,25,2020,'2023-07-12','kannur','Requested',''),(3,1,'revi','boat',123,111,100,2012,'2023-08-12','palakad','Verified','vessel verification.pdf'),(4,1,'revi','bnb',89098,345,50,2022,'2023-08-12','palakad','Requested','relief scheme 1.pdf');
/*!40000 ALTER TABLE `vessel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vessel_license`
--

DROP TABLE IF EXISTS `vessel_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vessel_license` (
  `vessel_license_id` int(11) NOT NULL AUTO_INCREMENT,
  `type of vessel` varchar(45) NOT NULL,
  `license type` varchar(45) NOT NULL,
  PRIMARY KEY (`vessel_license_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vessel_license`
--

LOCK TABLES `vessel_license` WRITE;
/*!40000 ALTER TABLE `vessel_license` DISABLE KEYS */;
INSERT INTO `vessel_license` VALUES (1,'mnkm','3year'),(2,'mnkm','3year'),(3,'ertytt','gghhj');
/*!40000 ALTER TABLE `vessel_license` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31 15:36:07
