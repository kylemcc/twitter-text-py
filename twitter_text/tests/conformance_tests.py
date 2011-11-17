import os
import unittest
import yaml

import twitter_text

BASE = os.path.dirname(__file__) or '.'
autolink = open(BASE + '/twitter-text-conformance/autolink.yml', 'r')
extract = open(BASE + '/twitter-text-conformance/extract.yml', 'r')
hit_highlight = open(BASE + '/twitter-text-conformance/hit_highlighting.yml', 'r')
validate = open(BASE + '/twitter-text-conformance/validate.yml', 'r')

extract_test_cases = yaml.load(extract)
autolink_test_cases = yaml.load(autolink)

class ExtractTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True

    def test_mentions_extractor_conformance(self):
        for case in extract_test_cases['tests']['mentions']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_mentioned_screen_names(),
                case['expected'],
                case['description'],
            )

    def test_mentions_with_indices_extractor_conformance(self):
        for case in extract_test_cases['tests']['mentions_with_indices']:
            #TODO: come up with a better way to test this...
            for e in case['expected']:
                e['indices'] = tuple(e['indices'])
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_mentioned_screen_names_with_indices(),
                case['expected'],
                case['description'],
            )

    def test_mentions_or_lists_with_indices_conformance(self):
        pass

    def test_replies_extractor_conformance(self):
        for case in extract_test_cases['tests']['replies']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_reply_screen_name(),
                case['expected'],
                case['description'],
            )

    def test_url_extractor_conformance(self):
        for case in extract_test_cases['tests']['urls']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_urls(),
                case['expected'],
                case['description'],
            )

    def test_urls_with_indices_extractor_conformance(self):
        for case in extract_test_cases['tests']['urls_with_indices']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_urls_with_indices(),
                case['expected'],
                case['description'],
            )

    def test_hashtag_extractor_conformance(self):
        for case in extract_test_cases['tests']['hashtags']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_hashtags(),
                case['expected'],
                case['description'],
            )

    def test_hashtags_with_indices_extractor_conformance(self):
        for case in extract_test_cases['tests']['hashtags_with_indices']:
            self.assertEqual(
                twitter_text.Extractor(case['text']).extract_hashtags_with_indices(),
                case['expected'],
                case['description'],
            )

class AutolinkTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True

    def test_users_autolink_conformance(self):
        for case in autolink_test_cases['tests']['usernames']:
            self.assertEqual(
                twitter_text.Autolink(case['text']).auto_link_usernames_or_lists(),
                case['expected'],
                case['description'],
            )

    def test_lists_autolink_conformance(self):
        for case in autolink_test_cases['tests']['lists']:
            self.assertEqual(
                twitter_text.Autolink(case['text']).auto_link_usernames_or_lists(),
                case['expected'],
                case['description'],
            )

    def test_urls_autolink_conformance(self):
        for case in autolink_test_cases['tests']['urls']:
            self.assertEqual(
                twitter_text.Autolink(case['text']).auto_link_urls_custom(),
                case['expected'],
                case['description'],
            )

    def test_hashtags_autolink_conformance(self):
        for case in autolink_test_cases['tests']['hashtags']:
            self.assertEqual(
                twitter_text.Autolink(case['text']).auto_link_hashtags(),
                case['expected'],
                case['description'],
            )

    def test_all_autolink_conformance(self):
        for case in autolink_test_cases['tests']['all']:
            self.assertEqual(
                twitter_text.Autolink(case['text']).auto_link(),
                case['expected'],
                case['description'],
            )

if __name__ == 'main':
    unittest.main()
