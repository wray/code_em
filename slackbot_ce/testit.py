import unittest
import bot_id
import slackpi
import wray.slacklib
import chris.slacklib
import joe.slacklib
import matthew.slacklib
import homeschool.baron.slacklib
import homeschool.elliot.slacklib
import homeschool.kaleb.slacklib
import homeschool.owen.slacklib
import homeschool.vivian.slacklib
import code_em.alec.slacklib
import code_em.coy.slacklib
import code_em.hadley.slacklib
import code_em.qiuqiu.slacklib
import code_em.zb.slacklib
import code_em.aidan.slacklib
import code_em.alex.slacklib
import code_em.taixi.slacklib
import code_em.al_kareem.slacklib

import code_em.anaya.slacklib
import code_em.mattias.slacklib
import code_em.travis.slacklib
import code_em.tyler.slacklib

import code_em.aaruv.slacklib
import code_em.anooshka.slacklib
import code_em.owen.slacklib
import code_em.patrick.slacklib
import code_em.summer.slacklib
import code_em.alec_r.slacklib

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_slack_client(self):
        self.assertTrue(bot_id.get_id() == None)

    def test_slack_pi(self):
        self.assertTrue(slackpi.handle_command("","") == None)

    def test_wray_handler(self):
        self.assertFalse(wray.slacklib.handle_command('') == None)
        self.assertTrue(len(wray.slacklib.handle_command(
            wray.slacklib.COMMAND1)) > 1)
        resp = wray.slacklib.handle_command(wray.slacklib.COMMAND4)
        print(resp)
        self.assertTrue(len(resp) > 1)

    def test_chris_handler(self):
        self.assertFalse(chris.slacklib.handle_command('') == None)
        self.assertTrue(len(chris.slacklib.handle_command(
            chris.slacklib.COMMAND1)) > 1)

    def test_joe_handler(self):
        self.assertFalse(joe.slacklib.handle_command('') == None)
        self.assertTrue(len(joe.slacklib.handle_command(
            joe.slacklib.COMMAND4)) > 1)
#        self.assertTrue(slackpi.handle_command(
#            joe.slacklib.COMMAND1,"") == None)
        #self.assertFalse(joe.slacklib.handle_command('green led on') == None)

    def test_matthew_handler(self):
        self.assertFalse(matthew.slacklib.handle_command('') == None)
        self.assertTrue(len(matthew.slacklib.handle_command(
            matthew.slacklib.COMMAND1)) > 1)

        
    def test_baron_handler(self):
        self.assertFalse(homeschool.baron.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.baron.slacklib.handle_command(
            homeschool.baron.slacklib.COMMAND1)) > 1)

    def test_elliot_handler(self):
        self.assertFalse(homeschool.elliot.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.elliot.slacklib.handle_command(
            homeschool.elliot.slacklib.COMMAND1)) > 1)

    def test_kaleb_handler(self):
        self.assertFalse(homeschool.kaleb.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.kaleb.slacklib.handle_command(
            homeschool.kaleb.slacklib.COMMAND1)) > 1)

#    def test_owen_handler(self):
#        self.assertFalse(homeschool.owen.slacklib.handle_command('') == None)
#        self.assertTrue(len(homeschool.owen.slacklib.handle_command(
#            homeschool.owen.slacklib.COMMAND1)) > 1)

    def test_vivian_handler(self):
        self.assertFalse(homeschool.vivian.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.vivian.slacklib.handle_command(
            homeschool.vivian.slacklib.COMMAND1)) > 1)


    def test_alec_handler(self):
        self.assertFalse(code_em.alec.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.alec.slacklib.handle_command(
            code_em.alec.slacklib.COMMAND1)) > 1)

    def test_coy_handler(self):
        self.assertFalse(code_em.coy.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.coy.slacklib.handle_command(
            code_em.coy.slacklib.COMMAND1)) > 1)

    def test_hadley_handler(self):
        self.assertFalse(code_em.hadley.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.hadley.slacklib.handle_command(
            code_em.hadley.slacklib.COMMAND1)) > 1)

    def test_qiuqiu_handler(self):
        self.assertFalse(code_em.qiuqiu.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.qiuqiu.slacklib.handle_command(
            code_em.qiuqiu.slacklib.COMMAND1)) > 1)

    def test_zb_handler(self):
        self.assertFalse(code_em.zb.slacklib.handle_command('') == None)
##        self.assertTrue(len(code_em.zb.slacklib.handle_command(
##            code_em.zb.slacklib.COMMAND1)) > 1)

    def test_aidan_handler(self):
        self.assertFalse(code_em.aidan.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.aidan.slacklib.handle_command(
            code_em.aidan.slacklib.COMMAND1)) > 1)

    def test_alex_handler(self):
        self.assertFalse(code_em.alex.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.alex.slacklib.handle_command(
            code_em.alex.slacklib.COMMAND1)) > 1)

    def test_taixi_handler(self):
        self.assertFalse(code_em.taixi.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.taixi.slacklib.handle_command(
            code_em.taixi.slacklib.COMMAND1)) > 1)

    def test_al_kareem_handler(self):
        self.assertFalse(code_em.al_kareem.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.al_kareem.slacklib.handle_command(
            code_em.al_kareem.slacklib.COMMAND1)) > 1)

    def test_anaya_handler(self):
        self.assertFalse(code_em.anaya.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.anaya.slacklib.handle_command(
            code_em.anaya.slacklib.COMMAND1)) > 1)

    def test_mattias_handler(self):
        self.assertFalse(code_em.mattias.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.mattias.slacklib.handle_command(
            code_em.mattias.slacklib.COMMAND1)) > 1)

    def test_travis_handler(self):
        self.assertFalse(code_em.travis.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.travis.slacklib.handle_command(
            code_em.travis.slacklib.COMMAND1)) > 1)

    def test_tyler_handler(self):
        self.assertFalse(code_em.tyler.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.tyler.slacklib.handle_command(
            code_em.tyler.slacklib.COMMAND1)) > 1)

    def test_aaruv_handler(self):
        self.assertFalse(code_em.aaruv.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.aaruv.slacklib.handle_command(
            code_em.aaruv.slacklib.COMMAND1)) > 1)

    def test_anooshka_handler(self):
        self.assertFalse(code_em.anooshka.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.anooshka.slacklib.handle_command(
            code_em.anooshka.slacklib.COMMAND1)) > 1)

    def test_owen_handler(self):
        self.assertFalse(code_em.owen.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.owen.slacklib.handle_command(
            code_em.owen.slacklib.COMMAND1)) > 1)

    def test_patrick_handler(self):
        self.assertFalse(code_em.patrick.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.patrick.slacklib.handle_command(
            code_em.patrick.slacklib.COMMAND1)) > 1)

    def test_summer_handler(self):
        self.assertFalse(code_em.summer.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.summer.slacklib.handle_command(
            code_em.summer.slacklib.COMMAND1)) > 1)

    def test_alec_r_handler(self):
        self.assertFalse(code_em.alec_r.slacklib.handle_command('') == None)
        self.assertTrue(len(code_em.alec_r.slacklib.handle_command(
            code_em.alec_r.slacklib.COMMAND1)) > 1)

    # def test_new_command_handler(self):
    #     self.assertTrue(wray.slacklib.handle_command("new command: how are you?, i'm fine thank you") == 'ok')
    #     self.assertTrue(wray.slacklib.handle_command('how are you?') == "i'm fine thank you")
    #     self.assertTrue(wray.slacklib.handle_command('del command: how are you?') == 'ok')
    #     self.assertFalse(wray.slacklib.handle_command('what!') == None)


if __name__ == '__main__':
    unittest.main()
