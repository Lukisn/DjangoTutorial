from datetime import timedelta

from django.utils import timezone
from django.urls import reverse
from django.test import TestCase

from .models import Question


def create_question(text, days):
    """Create a question with the given text and days offset to now."""
    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """Test function returns False on future question."""
        time = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """Test function returns False on question older than 1 day."""
        time = timezone.now() - timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        """Test function returns True on question from within the last day."""
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently())


class QuestionIndexViewTests(TestCase):

    def test_no_question(self):
        """Test an appropriate message is displayed if no question exists."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """Test past questions are displayed on the index page."""
        create_question(text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],
                                 ["<Question: Past question.>"])

    def test_future_question(self):
        """Test questions in the future aren't displayed on the index page."""
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        """Test only past questions are displayed."""
        create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Question: Past question.>'])

    def test_two_past_questions(self):
        """Test multiple past questions are displayed."""
        create_question(text="Past question 1.", days=-30)
        create_question(text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>'],
        )


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        """Test future questions aren't displayed in the details view."""
        future_question = create_question(text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """Test past questions are displayed in the details view."""
        past_question = create_question(text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):

    def test_future_question(self):
        """Test future questions aren't displayed in the results view."""
        future_question = create_question(text="Future question.", days=5)
        url = reverse("polls:results", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """Test past questions are displayed in the results view."""
        past_question = create_question(text="Past Question.", days=-5)
        url = reverse("polls:results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
