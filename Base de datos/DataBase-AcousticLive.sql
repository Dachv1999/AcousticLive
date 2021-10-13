-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: acousticlive
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `calificacion`
--

DROP TABLE IF EXISTS `calificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calificacion` (
  `idsuario` int NOT NULL,
  `cantidadEstrellas` int NOT NULL,
  KEY `fk_calificacion_usuario_idx` (`idsuario`),
  CONSTRAINT `fk_calificacion_usuario` FOREIGN KEY (`idsuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificacion`
--

LOCK TABLES `calificacion` WRITE;
/*!40000 ALTER TABLE `calificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `idcurso` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  PRIMARY KEY (`idcurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` VALUES (1,'basico','basiico'),(2,'medio','mediio'),(3,'avanzado','avanzaddo');
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leccion`
--

DROP TABLE IF EXISTS `leccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leccion` (
  `idleccion` int NOT NULL AUTO_INCREMENT,
  `idcurso` int NOT NULL,
  `nombreLeccion` varchar(45) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`idleccion`),
  KEY `fk_leccion_curso_idx` (`idcurso`),
  CONSTRAINT `fk_leccion_curso` FOREIGN KEY (`idcurso`) REFERENCES `curso` (`idcurso`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leccion`
--

LOCK TABLES `leccion` WRITE;
/*!40000 ALTER TABLE `leccion` DISABLE KEYS */;
INSERT INTO `leccion` VALUES (1,1,'acorde','aa'),(2,1,'familia de acordes','aaa'),(3,2,'tablatura','b'),(4,2,'lectura de tablatura','bbbb'),(5,3,'artegios','c'),(6,3,'escalas mayores','ccc');
/*!40000 ALTER TABLE `leccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pertenece`
--

DROP TABLE IF EXISTS `pertenece`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pertenece` (
  `idusuario` int NOT NULL,
  `idleccion` int NOT NULL,
  KEY `fk_pertenece_leccion_idx` (`idleccion`),
  KEY `fk_pertenece_calificacion_idx` (`idusuario`),
  CONSTRAINT `fk_pertenece_calificacion` FOREIGN KEY (`idusuario`) REFERENCES `calificacion` (`idsuario`),
  CONSTRAINT `fk_pertenece_leccion` FOREIGN KEY (`idleccion`) REFERENCES `leccion` (`idleccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pertenece`
--

LOCK TABLES `pertenece` WRITE;
/*!40000 ALTER TABLE `pertenece` DISABLE KEYS */;
/*!40000 ALTER TABLE `pertenece` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seinscribe`
--

DROP TABLE IF EXISTS `seinscribe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seinscribe` (
  `idusuario` int NOT NULL,
  `idcurso` int NOT NULL,
  KEY `fk_seInscribe_usuario_idx` (`idusuario`),
  KEY `fk_seInscribre_curso_idx` (`idcurso`),
  CONSTRAINT `fk_seInscribe_usuario` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`),
  CONSTRAINT `fk_seInscribre_curso` FOREIGN KEY (`idcurso`) REFERENCES `curso` (`idcurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seinscribe`
--

LOCK TABLES `seinscribe` WRITE;
/*!40000 ALTER TABLE `seinscribe` DISABLE KEYS */;
INSERT INTO `seinscribe` VALUES (1,1);
/*!40000 ALTER TABLE `seinscribe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  `nickName` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'juan','perez','1234','juan12','ddd@gmail.com'),(2,'ivan','monzon','12345','ivan12','i@gmail.com'),(3,'vale','flores','123456','vale12','v@gmail.com');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-13 15:55:27
