SELECT Department.NAME, COUNT(Employee.ID) AS COUNT_OF_EMPLOYEES_IN_THE_DEPARTMENT
/*selection le nom du departement  et compte le nombre d'id des employé qui sont compté comme étant employé dans le departement*/
FROM Department
LEFT JOIN Employee
/*en se basant de la jointure a gauche de la table employé*/
ON Department.ID = Employee.DEPT_ID
/* sur le id departement = a la clé etrangere de la table employé */
GROUP BY Department.NAME
/*regroupe tt les nom des departement */
ORDER BY COUNT_OF_EMPLOYEES_IN_THE_DEPARTMENT DESC, Department.NAME ASC;
/*et les trie le nombre des employé dans le departement en ordre decroissant*/
/*et le nom des departement en alphabetique*/