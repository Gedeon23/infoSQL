from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import Comment_Serializer, Comment_Tree_Serializer
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def comment_view(request, id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=id)
        return render(request, 'comment/detail.html', {'comment': comment})
    else:
        return redirect()


class Comment_Like_API(APIView):
    def get(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        user = self.request.user.profile
        if user in comment.likes.all():
            liked = False
            comment.likes.remove(user)
        else:
            liked = True
            comment.likes.add(user)

        like_count = comment.likes.count()
        data = {
            'updated': True,
            'liked': liked,
            'like_count': like_count
        }
        return Response(data)


class Comment_Comment_API(APIView):
    def post(self, request, id):
        parent_com = get_object_or_404(Comment, pk=id)
        user = self.request.user.profile
        content = self.request.POST.get('comment')
        comment = Comment(content=content, author=user,
                          post=parent_com.post, parent_comment=parent_com)
        comment.save()
        comments = get_list_or_404(Comment, parent_comment=parent_com)
        serialized = Comment_Serializer(comments, many=True)
        return Response(
            data={
                'success': True,
                'content': content,
                'comments': serialized.data
            }
        )


class Get_Comments_Comment_List(APIView):
    def get(self, request, id):
        parent_com = get_object_or_404(Comment, pk=id)
        comments = Comment.objects.filter(parent_comment=parent_com)
        coms_serialized = Comment_Serializer(comments, many=True)
        comment_tree = Comment_Tree_Serializer(parent_com)
        return Response(
            data={
                'message': 'easy',
                'comment_tree': comment_tree.data,
                'comments': coms_serialized.data
            }
        )
