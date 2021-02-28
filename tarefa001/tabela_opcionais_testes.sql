-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 28-Fev-2021 às 00:30
-- Versão do servidor: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portalerp`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tabela_opcionais_testes`
--

CREATE TABLE `tabela_opcionais_testes` (
  `codregistro` int(25) NOT NULL DEFAULT '0',
  `nome` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `sigla` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `unidade` decimal(10,0) NOT NULL DEFAULT '0',
  `ativo` int(1) NOT NULL DEFAULT '1',
  `observacao` text CHARACTER SET latin1
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

--
-- Extraindo dados da tabela `tabela_opcionais_testes`
--

INSERT INTO `tabela_opcionais_testes` (`codregistro`, `nome`, `sigla`, `unidade`, `ativo`, `observacao`) VALUES
(111, 'Vaso', 'V', '1', 1, 'This is a test.'),
(111, 'Adubo', 'A', '10', 1, 'This is a test two.'),
(111, 'Ração', 'R', '10', 1, 'Teste caracteres ração.'),
(111, 'Vaso04', 'V', '10', 0, 'Teste Inativo.');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
