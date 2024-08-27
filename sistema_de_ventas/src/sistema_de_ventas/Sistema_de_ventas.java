package sistema_de_ventas;

import sistema_de_ventas.views.login;

public class Sistema_de_ventas {

    public static void main(String[] args) {
        // TODO code application logic here
         // Establece la apariencia del sistema
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        // Muestra la ventana de login
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new login().setVisible(true);
            }
        });
    }
}