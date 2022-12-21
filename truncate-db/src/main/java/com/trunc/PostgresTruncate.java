package com.trunc;


import java.sql.*;
import java.util.ArrayList;


public class PostgresTruncate {

    public static void main(String[] args) {
        System.out.println("Required args: <localhost> <port> <dbName> <user> <pass>");
        System.out.println("Example: localhost 5432 testDB admin admin");

        String hostname = args[0];
        int port = Integer.parseInt(args[1]);
        String dbName = args[2];
        String user = args[3];
        String pass = args[4];


//        truncateDB("localhost", 5432, "test_db", "postgres", "253166");
        truncateDB(hostname, port, dbName, user, pass);
    }

    public static void truncateDB(String hostname,
                                  int port,
                                  String dbName,
                                  String user,
                                  String pass) {
        String url = "jdbc:postgresql://" + hostname + ":" + port + "/" + dbName;
        System.out.println("Connecting to '" + url + "' as '" + user + "'");
        try (Connection conn = DriverManager.getConnection(url, user, pass)) {
            System.out.println("Getting tables");
            ArrayList<String> allTables = getAllTables(conn);

            System.out.println("Truncating tables: " + allTables.size());
            for (String table : allTables) {
                truncateTable(conn, table);
            }

            System.out.println("Successfully truncated all tables in DB");
        } catch (SQLException e) {
            System.err.println("Failed to connect to '" + url + "' as '" + user + "'");
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    private static ArrayList<String> getAllTables(Connection conn) {
        String TABLE_COLUMN_NAME = "table_name";
        ArrayList<String> tables = new ArrayList<>();
        String sql = "select *  FROM information_schema.tables where table_schema = 'public'";
        try (Statement st = conn.createStatement()) {

            System.out.println("Executing select: " + sql);
            ResultSet rs = st.executeQuery(sql);

            while (rs.next()) {
                tables.add(rs.getString(TABLE_COLUMN_NAME));
            }
        } catch (SQLException e) {
            System.err.println("Failed to get all 'public' tables: " + sql);
            e.printStackTrace();
            throw new RuntimeException(e);
        }
        return tables;
    }

    private static void truncateTable(Connection conn, String tableName) {
        String sql = "truncate table " + tableName + " CASCADE";
        try (Statement st = conn.createStatement()) {
            System.out.println("Executing truncate for table '" + tableName + "': " + sql);
            st.execute(sql);
        } catch (SQLException e) {
            System.err.println("Failed to truncate table: " + sql);
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

}
