-- 1. Creación de la base de datos
CREATE DATABASE IF NOT EXISTS db_recetas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- 2. Creación del usuario del sistema
CREATE USER IF NOT EXISTS 'admin_recetas'@'localhost' IDENTIFIED BY 'recetas2026';

-- 3. Asignación de permisos sobre la base de datos
GRANT ALL PRIVILEGES ON db_recetas.* TO 'admin_recetas'@'localhost';

-- 4. Aplicar cambios en los privilegios
FLUSH PRIVILEGES;