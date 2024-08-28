-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-08-2024 a las 08:12:28
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `api_restful_ed2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accesshistory`
--

CREATE TABLE `accesshistory` (
  `accessHistoryId` int(11) NOT NULL,
  `adminId` int(11) DEFAULT NULL,
  `accessTime` datetime NOT NULL DEFAULT current_timestamp(),
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `accesshistory`
--

INSERT INTO `accesshistory` (`accessHistoryId`, `adminId`, `accessTime`, `state`) VALUES
(1, 1, '2024-08-28 01:09:32', 'success'),
(2, NULL, '2024-08-28 01:11:00', 'failure');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accesshistory`
--
ALTER TABLE `accesshistory`
  ADD PRIMARY KEY (`accessHistoryId`),
  ADD KEY `fk_adminId` (`adminId`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accesshistory`
--
ALTER TABLE `accesshistory`
  MODIFY `accessHistoryId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `accesshistory`
--
ALTER TABLE `accesshistory`
  ADD CONSTRAINT `fk_adminId` FOREIGN KEY (`adminId`) REFERENCES `admins` (`adminId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
