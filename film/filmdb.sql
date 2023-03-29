-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 29 mars 2023 à 05:06
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `filmdb`
--

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

DROP TABLE IF EXISTS `film`;
CREATE TABLE IF NOT EXISTS `film` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(255) NOT NULL,
  `duree` int(11) NOT NULL,
  `Realisateur` varchar(255) NOT NULL,
  `synopsis` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`id`, `titre`, `duree`, `Realisateur`, `synopsis`) VALUES
(1, 'Dune', 155, 'Denis Villeneuve', 'Un prince exilé doit récupérer le contrôle d\'une planète désertique riche en épice'),
(2, 'The French Dispatch', 108, 'Wes Anderson', 'Un journaliste américain basé en France couvre des histoires excentriques pour son magazine'),
(3, 'Licorice Pizza', 133, 'Paul Thomas Anderson', 'Deux adolescents poursuivent leurs rêves à Los Angeles dans les années 1970'),
(4, 'Don\'t Look Up', 138, 'Adam McKay', 'Deux astronomes tentent d\'avertir le monde de la collision imminente d\'un astéroïde avec la Terre'),
(5, 'Spencer', 112, 'Pablo Larraín', 'Un portrait imaginaire de la Princesse Diana lors d\'un week-end de Noël en 1991'),
(6, 'West Side Story', 156, 'Steven Spielberg', 'Une réinvention du classique musical de Broadway situé dans les années 1950 à New York'),
(7, 'The Power of the Dog', 126, 'Jane Campion', 'Un cowboy manipulateur tourmente son frère et sa belle-sœur après leur mariage'),
(8, 'Belfast', 97, 'Kenneth Branagh', 'Un jeune garçon grandit dans les années 1960 à Belfast, en Irlande du Nord'),
(9, 'The Lost Daughter', 120, 'Maggie Gyllenhaal', 'Une universitaire en vacances en Grèce rencontre une famille avec des secrets'),
(10, 'Benediction', 111, 'Terence Davies', 'La vie du poète anglais Siegfried Sassoon pendant la Première Guerre mondiale'),
(11, 'The Humans', 108, 'Stephen Karam', 'Une famille de classe moyenne rencontre des difficultés lors d\'un repas de Thanksgiving'),
(12, 'C\'est la vie', 99, 'Julie Delpy', 'Une femme doit jongler avec sa famille, son travail et ses problèmes de santé mentale');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
