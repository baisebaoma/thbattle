# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
# -- own --
from thb import cards, characters
from thb.ui.ui_meta.common import gen_metafunc, passive_clickable, passive_is_action_valid

# -- code --
__metaclass__ = gen_metafunc(characters.nazrin)


class Nazrin:
    # Character
    name        = u'纳兹琳'
    title       = u'探宝的小小大将'
    illustrator = u'月见'
    cv          = u'小羽'

    port_image        = u'thb-portrait-nazrin'
    figure_image      = u'thb-figure-nazrin'
    miss_sound_effect = u'thb-cv-nazrin_miss'


class NazrinKOF:
    # Character
    name        = u'纳兹琳'
    title       = u'探宝的小小大将'
    illustrator = u'月见'
    cv          = u'小羽'

    port_image        = u'thb-portrait-nazrin'
    figure_image      = u'thb-figure-nazrin'
    miss_sound_effect = u'thb-cv-nazrin_miss'

    notes = u'|RKOF修正角色|r'


class TreasureHunt:
    # Skill
    name = u'探宝'
    description = u'准备阶段开始时，你可以进行一次判定，若结果为黑，你获得此牌且你可以重复此流程。'

    clickable = passive_clickable
    is_action_valid = passive_is_action_valid


class TreasureHuntHandler:
    # choose_option
    choose_option_buttons = ((u'发动', True), (u'不发动', False))
    choose_option_prompt = u'你要发动【探宝】吗？'


class Agile:
    # Skill
    name = u'轻敏'
    description = u'你可以将一张黑色手牌当|G擦弹|r使用或打出。'

    def clickable(game):
        me = game.me

        try:
            act = game.action_stack[-1]
        except IndexError:
            return False

        if isinstance(act, cards.BaseUseGraze) and (me.cards or me.showncards):
            return True

        return False

    def is_complete(g, cl):
        skill = cl[0]
        cl = skill.associated_cards
        if len(cl) != 1:
            return (False, u'请选择一张牌！')
        else:
            c = cl[0]
            if c.resides_in not in (g.me.cards, g.me.showncards):
                return (False, u'请选择手牌！')
            if c.suit not in (cards.Card.SPADE, cards.Card.CLUB):
                return (False, u'请选择一张黑色的牌！')
            return (True, u'这种三脚猫的弹幕，想要打中我是不可能的啦~')

    def sound_effect(act):
        return 'thb-cv-nazrin_agile'


class AgileKOF:
    # Skill
    name = u'轻敏'
    description = u'你可以将一张|B黑桃|r手牌当|G擦弹|r使用或打出。'

    clickable = Agile['clickable']

    def is_complete(g, cl):
        skill = cl[0]
        cl = skill.associated_cards
        if len(cl) != 1:
            return (False, u'请选择一张牌！')
        else:
            c = cl[0]
            if c.resides_in not in (g.me.cards, g.me.showncards):
                return (False, u'请选择手牌！')
            if c.suit != cards.Card.SPADE:
                return (False, u'请选择一张黑桃色手牌牌！')
            return (True, u'这种三脚猫的弹幕，想要打中我是不可能的啦~')

    sound_effect = Agile['sound_effect']


class TreasureHuntAction:
    fatetell_display_name = u'探宝'

    def effect_string(act):
        if act.succeeded:
            return u'|G【%s】|r找到了|G%s|r。' % (
                act.target.ui_meta.name,
                act.card.ui_meta.name,
            )
        else:
            return u'|G【%s】|r什么也没有找到…' % (
                act.target.ui_meta.name,
            )

    def sound_effect(act):
        tgt = act.target
        t = tgt.tags
        if not t['__treasure_hunt_se'] >= t['turn_count']:
            t['__treasure_hunt_se'] = t['turn_count']
            return 'thb-cv-nazrin_treasurehunt'
